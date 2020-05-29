import datetime
import os
import shutil
import csv

import torch
import numpy as np
import torch.nn.functional as F

from tqdm import tqdm, trange


def make_dir(dir_path):
    """
    Makes a directory if already doesn't exist
    :param dir_path: Directory path to be created
    :return: Directory path (str)
    """
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    return dir_path


def set_seed(seed):
    """
    Set model random seed. The model outputs are seed dependent.
    :param seed: An int.
    :return: No return
    """
    np.random.seed(seed)
    torch.random.manual_seed(seed)
    torch.cuda.manual_seed(seed)


def get_device(logger):
    """
    Get device model will be run on (GPU or CPU)
    :param logger: Logger object to note the device
    :return: device type, num_of_gpus
    """
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    n_gpu = torch.cuda.device_count()
    logger.info("device: {}, n_gpu {}".format(device, n_gpu))
    return device, n_gpu


def create_save_path(args, execution_file_path):
    """
    1) Constructs a model save path: "master_dir/(optional folder)/train_data_name/model_size__date)"
    2) Creates a copy of the main code.
    :param args: Model arguments object
    :param execution_file_path: file path to the main code
    :return: Training specific directory where everything will be saved to.
    """
    now = datetime.datetime.now().strftime("%d-%m-%Y@%H'%M")
    master_dir = os.path.dirname(execution_file_path)
    # Extract dataset file name from the full path
    dataset_name = os.path.basename(os.path.normpath(args.train_data_path)).split(".")[0]

    if args.store_in_folder:
        log_path = "{}/{}/{}/{}_{}".format(master_dir, args.store_in_folder, dataset_name, args.model_size, now)
    else:
        log_path = "{}/{}/{}_{}".format(master_dir, dataset_name, args.model_size, now)
    make_dir(log_path)

    # COPY OF THE MAIN CODE
    shutil.copy2(execution_file_path, "{}/copy_of_code_that_run_this_experiment.py".format(log_path))
    return log_path


def log_arguments(run_details_file_path, args, special_tokens):
    """
    Saves training information to a file, like arguments and special tokens.
    :param run_details_file_path: File to be written to
    :param args: Model arguments object
    :param special_tokens: Special tokens used in this training
    :return: No return
    """
    now = datetime.datetime.now().strftime("%d-%m-%Y@%H'%M")
    # Open a file and appends to a file. If doesn't exists (+) means to create it.
    d_file = open(run_details_file_path, "a+")
    d_file.write("@" * 30 + " RUN INFO " + "@" * 30)
    d_file.write("\n\nDATE: {}".format(now))
    d_file.write("\n\nUSING THE FOLLOWING ARGS:\n{}".format(args))
    d_file.write("\n\nSPECIAL TOKENS: {}".format(special_tokens))
    d_file.close()


def save_dataset(path, input, append=True):
    """
    Saves data to a file path.
    :param path: Save file path
    :param input: Data to be saved
    :param append: Whether we should append data or write to clean file
    :return: No return
    """
    if append:
        with open(path, 'a+', encoding='utf_8') as f:
            writer = csv.writer(f)
            writer.writerows(input)
    else:
        with open(path, 'w+', encoding='utf_8') as f:
            writer = csv.writer(f)
            writer.writerows(input)
    f.close()


def load_dataset(dataset_path):
    """
    Loads lyrics dataset of the following format (genre, artist, year, album, song_name, lyrics)
    :param dataset_path: Dataset file path (type csv)
    :return: List of tuples where each entry contains a song and its metadata
    """
    with open(dataset_path, encoding='utf_8') as f:
        f = csv.reader(f)
        output = []
        for line in tqdm(f):
            # Output      (genre,   artist,   year,   album,  song_name, lyrics)
            output.append((line[0], line[1], line[2], line[3], line[4], line[5]))
    return output


def format_n_tokenize_data(raw_dataset, enc):
    """
    Seperates metadata with respective special tokens and then tokenizes the formated text
    :param raw_dataset: Text to format and style
    :param enc: Tokenizer object
    :return: Formated data in the form of tuples
    """
    ### TODO: make training examples where lyrics are as a condition to predict features

    # Get the dict: special token -> token id
    spe = enc.added_tokens_encoder

    formated_data = []
    for genre, artist, year, album, song_name, lyrics in raw_dataset:
        ge = [spe["[s:genre]"]] + enc.encode(genre) + [spe["[e:genre]"]]
        ar = [spe["[s:artist]"]] + enc.encode(artist) + [spe["[e:artist]"]]
        ye = [spe["[s:year]"]] + enc.encode(year) + [spe["[e:year]"]]
        al = [spe["[s:album]"]] + enc.encode(album) + [spe["[e:album]"]]
        sn = [spe["[s:song_name]"]] + enc.encode(song_name) + [spe["[e:song_name]"]]
        ly = [spe["[s:lyrics]"]] + enc.encode(lyrics) + [spe["[e:lyrics]"]]

        formated_data.append((ge, ar, ye, al, sn, ly))

    print("The exceeding in length inputs are removed from the dataset.")
    return formated_data


def construct_input(formated_data, device, max_input_len=1024):
    """
    Given a tokenized dataset, this method constructs inputs required for the GPT2 model fine-tuning.
    In particular, it creates token_type_ids & positional_ids, randomly drops lyrics' features, applies padding and
    creates language modelling labels, as well as the attention masks.
    Refer to - https://huggingface.co/transformers/model_doc/gpt2.html#gpt2lmheadmodel - for an indication of the inputs
    :param formated_data: Tokenised dataset with special tokens inplace provided in the form of tuple(all song features)
    :param device: Device that will run this code (GPU, CPU)
    :param max_input_len: Max input length allowed by the model
    :return: Tuple of tensors: (token_ids, token_type_ids, position_ids, attention_mask, lm_labels)
             where each is of shape: (num_of_inputs * batch_size * sequence_length) -> (N, 1, 1024)
    """
    sucessfull_candidates = []
    for genre, artist, year, album, song_name, lyrics in formated_data:
        # 1) Prepare input partitions, i.e., token type ids & position ids
        # Token type ids, alternatively called segment ids
        gen_seg = list([1] * len(genre))
        art_seg = list([2] * len(artist))
        yea_seg = list([3] * len(year))
        alb_seg = list([4] * len(album))
        son_seg = list([5] * len(song_name))
        lyr_seg = list([6] * len(lyrics))

        # 2) Randomly drop features for model to learn to handle subset of conditions
        # 25% to drop all metadata but lyrics
        if np.random.rand() <= 0.25:
            # An integer sequence (0 -> input_len)
            position_ids = list(np.arange(0, len(lyrics)))
            curr_input = {
                "tok_ids": lyrics,
                "tok_type_ids": lyr_seg,
                "pos_ids": position_ids
            }
        # 10% of dropping the individual features
        else:
            tokens_subset = []
            segment_subset = []

            if np.random.rand() > 0.1:
                tokens_subset += genre
                segment_subset += gen_seg

            if np.random.rand() > 0.1:
                tokens_subset += artist
                segment_subset += art_seg

            if np.random.rand() > 0.1:
                tokens_subset += year
                segment_subset += yea_seg

            if np.random.rand() > 0.1:
                tokens_subset += album
                segment_subset += alb_seg

            if np.random.rand() > 0.1:
                tokens_subset += song_name
                segment_subset += son_seg

            # Add lyrics in all cases -> add lyrics
            tokens_subset += lyrics
            segment_subset += lyr_seg
            position_ids = list(np.arange(0, len(tokens_subset)))

            curr_input = {
                "tok_ids": tokens_subset,
                "tok_type_ids": segment_subset,
                "pos_ids": position_ids
            }

        # Get rid of songs longer than allowed size, alternatively we could cut off the excess
        if len(curr_input["tok_ids"]) > max_input_len:
            continue

        # 3) Add padding to make the input max_input_len
        len_before_padding = len(curr_input["tok_ids"])
        padding = max_input_len - len_before_padding

        curr_input["tok_ids"] += list([0] * padding)
        curr_input["tok_type_ids"] += list([0] * padding)
        curr_input["pos_ids"] += list([0] * padding)

        # 4) Language Modelling Labels -> this is input_copy with padding assigned to -1,
        #    the position shifting is done in the library code.
        lm_labels = np.copy(curr_input["tok_ids"])
        lm_labels[np.where(lm_labels == 0)] = -1

        # 5) Attention Mask, 1 = unmasked, 0 = masked
        attention_mask = list([1] * len_before_padding) + list([0] * padding)

        sucessfull_candidates.append((
            curr_input["tok_ids"], curr_input["tok_type_ids"], curr_input["pos_ids"], attention_mask, lm_labels
        ))

    # We need the model inputs separate for the DataLoader
    # From tuples of (N, 5, 1024) -> (N, 1024) x 5
    # Note: inputs contains 5 lists
    inputs = map(list, zip(*sucessfull_candidates))

    # Transform each input into a tensor of shape:
    # (num_inputs, batch_size, sequence_len) -> (N, 1, 1024)
    dataset = [torch.tensor(t, device=torch.device(device)).unsqueeze(1) for t in inputs]

    return dataset


def top_k_top_p_filtering(logits, top_k=0, top_p=0.0, filter_value=-float('Inf')):
    """
    Filter a distribution of logits using top-k and/or nucleus (top-p) filtering.
    Nucleus filtering is described in Holtzman et al. (http://arxiv.org/abs/1904.09751)
    From: https://gist.github.com/thomwolf/1a5a29f6962089e871b94cbd09daf317
    :param logits: Logits distribution shape (batch size x vocabulary size)
    :param top_k: Keep only top k tokens with highest probability (top-k filtering).
    :param top_p: Keep the top tokens with cumulative probability >= top_p (nucleus filtering).
    :param filter_value: Value that will be ignored by in the softmax
    :return: Filtered logits
    """

    top_k = min(top_k, logits.size(-1))  # Safety check
    if top_k > 0:
        # Remove all tokens with a probability less than the last token of the top-k
        indices_to_remove = logits < torch.topk(logits, top_k)[0][..., -1, None]
        logits[indices_to_remove] = filter_value

    if top_p > 0.0:
        sorted_logits, sorted_indices = torch.sort(logits, descending=True)
        cumulative_probs = torch.cumsum(F.softmax(sorted_logits, dim=-1), dim=-1)

        # Remove tokens with cumulative probability above the threshold
        sorted_indices_to_remove = cumulative_probs > top_p
        # Shift the indices to the right to keep also the first token above the threshold
        sorted_indices_to_remove[..., 1:] = sorted_indices_to_remove[..., :-1].clone()
        sorted_indices_to_remove[..., 0] = 0

        # scatter sorted tensors to original indexing
        indices_to_remove = sorted_indices_to_remove.scatter(dim=1, index=sorted_indices, src=sorted_indices_to_remove)
        logits[indices_to_remove] = filter_value
    return logits


meta_dict = {
      "genre": {
          "st_token": "[s:genre]",
          "end_token": "[e:genre]",
          "tok_type_id": 1
      },
      "artist": {
          "st_token": "[s:artist]",
          "end_token": "[e:artist]",
          "tok_type_id": 2
      },
      "year": {
          "st_token": "[s:year]",
          "end_token": "[e:year]",
          "tok_type_id": 3
      },
      "album": {
          "st_token": "[s:album]",
          "end_token": "[e:album]",
          "tok_type_id": 4
      },
      "song_name": {
          "st_token": "[s:song_name]",
          "end_token": "[e:song_name]",
          "tok_type_id": 5
      },
      "lyrics": {
          "st_token": "[s:lyrics]",
          "end_token": "[e:lyrics]",
          "tok_type_id": 6
      }
}
  

def construct_conditions(conds_dict):
  context = ""
  for cond in conds_dict.keys():
      if cond is not "lyrics":
          # Check whether the condition exists
          if conds_dict[cond] is not "None":
              cut_index = conds_dict[cond].find("(")
              # If there is something to cut out
              if cut_index is not -1:
                  wrapped_cond = meta_dict[cond]["st_token"] + conds_dict[cond][:cut_index-1] + meta_dict[cond]["end_token"]
              else:
                  wrapped_cond = meta_dict[cond]["st_token"] + conds_dict[cond] + meta_dict[cond]["end_token"]
              
              context += wrapped_cond
      else:
          # Special case that doesnt required end token
          wrapped_cond = meta_dict[cond]["st_token"] + conds_dict[cond]
          context += wrapped_cond
    
  return context


def get_token_types(input, enc):
    """
    This method generates toke_type_ids that correspond to the given input_ids.
    :param input: Input_ids (tokenised input)
    :param enc: Model tokenizer object
    :return: A list of toke_type_ids corresponding to the input_ids
    """
    tok_type_ids = [0] * len(input)

    for feature in meta_dict.keys():
        start_tok_id = enc.added_tokens_encoder[meta_dict[feature]["st_token"]]
        end_tok_id = enc.added_tokens_encoder[meta_dict[feature]["end_token"]]
        tok_type_val = meta_dict[feature]["tok_type_id"]

        # If this feature exists in the input, find out its indexes
        if start_tok_id and end_tok_id in input:
            st_indx = input.index(start_tok_id)
            end_indx = input.index(end_tok_id)
            tok_type_ids[st_indx:end_indx+1] = [tok_type_val] * ((end_indx-st_indx) + 1)
        # This means that this is the token we are currently predicting
        elif start_tok_id in input:
            st_indx = input.index(start_tok_id)
            tok_type_ids[st_indx:] = [tok_type_val] * (len(input)-st_indx)

    return tok_type_ids


def generate_lyrics(model, enc, GEN_BATCH, context, end_token, device):
    """
    Generates a sequence of words from the fine-tuned model, token by token. This method generates with the
    token_type_ids and position_ids -> since the fine-tuned model is trained with the former input partitions.
    Note: When generating with the 'past', it is required to pass the single generated token only, without
    the previous tokens (not the concatination of the previous input + the generated token).
    :param model: Loaded fine-tune model object
    :param enc: Loaded tokenizer object
    :param GEN_BATCH: Generative batch size
    :param context: Tokenized input_ids on which the output generations will be based on.
    :param end_token: Signal to cut off further generation, e.g., [e:lyrics]
    :param device: Device on which the model will be run on
    :return: Generated lyrics along with the condition provided.
    """
    # Pack in tensor and correct shape
    input_ids = torch.tensor(context, device=device, dtype=torch.long).unsqueeze(0).repeat(GEN_BATCH, 1)
    position_ids = torch.arange(0, len(context), device=device, dtype=torch.long).unsqueeze(0).repeat(GEN_BATCH, 1)
    token_type_ids = torch.tensor(get_token_types(context, enc), device=device, dtype=torch.long).unsqueeze(0).repeat(GEN_BATCH, 1)
    
    # 'Output' stores the concatination of word by word prediction
    output = input_ids.tolist()

    # Get the end of generation signal, token_id of, e.g., [e:lyrics]
    end_token_id = enc.added_tokens_encoder[end_token]
    max_len = enc.max_len

    with torch.no_grad():
        past = None
        keep_gen_4_these_batches = np.arange(0, GEN_BATCH).tolist()
        for _ in trange(len(context), max_len):
            logits, past = model(input_ids=input_ids,
                                 position_ids=position_ids,
                                 token_type_ids=token_type_ids,
                                 past=past)

            next_token_logits = logits[:, -1, :]
            filtered_logits = top_k_top_p_filtering(next_token_logits, top_k=0, top_p=0.95)
            log_probs = F.softmax(filtered_logits, dim=-1)
            next_token_id = torch.multinomial(log_probs, num_samples=1)

            # Since we are using past, the model only requires the generated token as the next input
            input_ids = next_token_id
            position_ids = torch.tensor(len(output[0]), device=device, dtype=torch.long).unsqueeze(0).repeat(GEN_BATCH, 1)
            # What ever was the last element we want the same value for the next toke_type_id
            token_type_ids = torch.tensor(token_type_ids[0][-1].item(), device=device, dtype=torch.long).unsqueeze(0).repeat(GEN_BATCH, 1)

            # The gen should stop when the end tag reached; however, we can predict a few songs at a time (batch).
            # Solution: keep generating until model predicts the end signal for ALL batch indexes, but, only append
            # the predicted tokens to batch indexes that have not seen the end signal yet.
            if len(keep_gen_4_these_batches) > 0:
                for batch_indx in keep_gen_4_these_batches:
                    output[batch_indx].append(next_token_id[batch_indx].item())

                    if next_token_id[batch_indx].item() == end_token_id:
                        indx = keep_gen_4_these_batches.index(batch_indx)
                        keep_gen_4_these_batches.pop(indx)
            else:
                # Break out when predicted end signal for all batch indexes
                break

    return output
