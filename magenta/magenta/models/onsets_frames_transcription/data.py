# Copyright 2019 The Magenta Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Shared methods for providing data to transcription models.

Glossary (definitions may not hold outside of this particular file):
  sample: The value of an audio waveform at a discrete timepoint.
  frame: An individual row of a constant-Q transform computed from some
      number of audio samples.
  example: An individual training example. The number of frames in an example
      is determined by the sequence length.
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import functools
import wave
import zlib

import librosa
from magenta.models.onsets_frames_transcription import audio_transform
from magenta.models.onsets_frames_transcription import constants
from magenta.music import audio_io
from magenta.music import melspec_input
from magenta.music import sequences_lib
from magenta.protobuf import music_pb2
import numpy as np
import six
import tensorflow as tf
import tensorflow_probability as tfp


def hparams_frame_size(hparams):
  """Find the frame size of the input conditioned on the input type."""
  if hparams.spec_type == 'raw':
    return hparams.spec_hop_length
  return hparams.spec_n_bins


def hparams_frames_per_second(hparams):
  """Compute frames per second as a function of HParams."""
  return hparams.sample_rate / hparams.spec_hop_length


def _wav_to_cqt(wav_audio, hparams):
  """Transforms the contents of a wav file into a series of CQT frames."""
  y = audio_io.wav_data_to_samples(wav_audio, hparams.sample_rate)

  cqt = np.abs(
      librosa.core.cqt(
          y,
          hparams.sample_rate,
          hop_length=hparams.spec_hop_length,
          fmin=hparams.spec_fmin,
          n_bins=hparams.spec_n_bins,
          bins_per_octave=hparams.cqt_bins_per_octave),
      dtype=np.float32)

  # Transpose so that the data is in [frame, bins] format.
  cqt = cqt.T
  return cqt


def _wav_to_mel(wav_audio, hparams):
  """Transforms the contents of a wav file into a series of mel spec frames."""
  y = audio_io.wav_data_to_samples(wav_audio, hparams.sample_rate)

  mel = librosa.feature.melspectrogram(
      y,
      hparams.sample_rate,
      hop_length=hparams.spec_hop_length,
      fmin=hparams.spec_fmin,
      n_mels=hparams.spec_n_bins,
      htk=hparams.spec_mel_htk).astype(np.float32)

  # Transpose so that the data is in [frame, bins] format.
  mel = mel.T
  return mel


def _wav_to_framed_samples(wav_audio, hparams):
  """Transforms the contents of a wav file into a series of framed samples."""
  y = audio_io.wav_data_to_samples(wav_audio, hparams.sample_rate)

  hl = hparams.spec_hop_length
  n_frames = int(np.ceil(y.shape[0] / hl))
  frames = np.zeros((n_frames, hl), dtype=np.float32)

  # Fill in everything but the last frame which may not be the full length
  cutoff = (n_frames - 1) * hl
  frames[:n_frames - 1, :] = np.reshape(y[:cutoff], (n_frames - 1, hl))
  # Fill the last frame
  remain_len = len(y[cutoff:])
  frames[n_frames - 1, :remain_len] = y[cutoff:]

  return frames


def wav_to_spec(wav_audio, hparams):
  """Transforms the contents of a wav file into a series of spectrograms."""
  if hparams.spec_type == 'raw':
    spec = _wav_to_framed_samples(wav_audio, hparams)
  else:
    if hparams.spec_type == 'cqt':
      spec = _wav_to_cqt(wav_audio, hparams)
    elif hparams.spec_type == 'mel':
      spec = _wav_to_mel(wav_audio, hparams)
    else:
      raise ValueError('Invalid spec_type: {}'.format(hparams.spec_type))

    if hparams.spec_log_amplitude:
      spec = librosa.power_to_db(spec)

  return spec


def wav_to_spec_op(wav_audio, hparams):
  spec = tf.py_func(
      functools.partial(wav_to_spec, hparams=hparams),
      [wav_audio],
      tf.float32,
      name='wav_to_spec')
  spec.set_shape([None, hparams_frame_size(hparams)])
  return spec


MELSPEC_SAMPLE_RATE = 16000


def tflite_compat_mel(wav_audio, hparams):
  """EXPERIMENTAL: Log mel spec with ops that can be made TFLite compatible."""
  samples, decoded_sample_rate = tf.audio.decode_wav(
      wav_audio, desired_channels=1)
  samples = tf.squeeze(samples, axis=1)
  with tf.control_dependencies(
      [tf.assert_equal(decoded_sample_rate, MELSPEC_SAMPLE_RATE)]):
    features = melspec_input.build_mel_calculation_graph(
        samples, MELSPEC_SAMPLE_RATE,
        window_length_seconds=2048 / MELSPEC_SAMPLE_RATE,  # 0.128
        hop_length_seconds=(
            hparams.spec_hop_length / MELSPEC_SAMPLE_RATE),  # 0.032
        num_mel_bins=hparams.spec_n_bins,
        lower_edge_hz=hparams.spec_fmin,
        upper_edge_hz=MELSPEC_SAMPLE_RATE / 2.0,
        frame_width=1,
        frame_hop=1,
        tflite_compatible=False)  # False here, but would be True on device.
    return tf.squeeze(features, 1)


def get_spectrogram_hash_op(spectrogram):
  """Calculate hash of the spectrogram."""
  def get_spectrogram_hash(spectrogram):
    # Compute a hash of the spectrogram, save it as an int64.
    # Uses adler because it's fast and will fit into an int (md5 is too large).
    spectrogram_serialized = six.BytesIO()
    np.save(spectrogram_serialized, spectrogram)
    spectrogram_hash = np.int64(zlib.adler32(spectrogram_serialized.getvalue()))
    return spectrogram_hash
  spectrogram_hash = tf.py_func(get_spectrogram_hash, [spectrogram], tf.int64,
                                name='get_spectrogram_hash')
  spectrogram_hash.set_shape([])
  return spectrogram_hash


def wav_to_num_frames(wav_audio, frames_per_second):
  """Transforms a wav-encoded audio string into number of frames."""
  w = wave.open(six.BytesIO(wav_audio))
  return np.int32(w.getnframes() / w.getframerate() * frames_per_second)


def wav_to_num_frames_op(wav_audio, frames_per_second):
  """Transforms a wav-encoded audio string into number of frames."""
  res = tf.py_func(
      functools.partial(wav_to_num_frames, frames_per_second=frames_per_second),
      [wav_audio],
      tf.int32,
      name='wav_to_num_frames_op')
  res.set_shape(())
  return res


def transform_wav_data_op(wav_data_tensor, hparams, jitter_amount_sec):
  """Transforms with audio for data augmentation. Only for training."""

  def transform_wav_data(wav_data):
    """Transforms with sox."""
    if jitter_amount_sec:
      wav_data = audio_io.jitter_wav_data(wav_data, hparams.sample_rate,
                                          jitter_amount_sec)
    wav_data = audio_transform.transform_wav_audio(wav_data, hparams)

    return [wav_data]

  return tf.py_func(
      transform_wav_data, [wav_data_tensor],
      tf.string,
      name='transform_wav_data_op')


def sequence_to_pianoroll_op(sequence_tensor, velocity_range_tensor, hparams):
  """Transforms a serialized NoteSequence to a pianoroll."""

  def sequence_to_pianoroll_fn(sequence_tensor, velocity_range_tensor):
    """Converts sequence to pianorolls."""
    velocity_range = music_pb2.VelocityRange.FromString(velocity_range_tensor)
    sequence = music_pb2.NoteSequence.FromString(sequence_tensor)
    sequence = sequences_lib.apply_sustain_control_changes(sequence)
    roll = sequences_lib.sequence_to_pianoroll(
        sequence,
        frames_per_second=hparams_frames_per_second(hparams),
        min_pitch=constants.MIN_MIDI_PITCH,
        max_pitch=constants.MAX_MIDI_PITCH,
        min_frame_occupancy_for_label=hparams.min_frame_occupancy_for_label,
        onset_mode=hparams.onset_mode,
        onset_length_ms=hparams.onset_length,
        offset_length_ms=hparams.offset_length,
        onset_delay_ms=hparams.onset_delay,
        min_velocity=velocity_range.min,
        max_velocity=velocity_range.max)
    return (roll.active, roll.weights, roll.onsets, roll.onset_velocities,
            roll.offsets)

  res, weighted_res, onsets, velocities, offsets = tf.py_func(
      sequence_to_pianoroll_fn, [sequence_tensor, velocity_range_tensor],
      [tf.float32, tf.float32, tf.float32, tf.float32, tf.float32],
      name='sequence_to_pianoroll_op')
  res.set_shape([None, constants.MIDI_PITCHES])
  weighted_res.set_shape([None, constants.MIDI_PITCHES])
  onsets.set_shape([None, constants.MIDI_PITCHES])
  offsets.set_shape([None, constants.MIDI_PITCHES])
  velocities.set_shape([None, constants.MIDI_PITCHES])

  return res, weighted_res, onsets, offsets, velocities


def jitter_label_op(sequence_tensor, jitter_amount_sec):

  def jitter_label(sequence_tensor):
    sequence = music_pb2.NoteSequence.FromString(sequence_tensor)
    sequence = sequences_lib.shift_sequence_times(sequence, jitter_amount_sec)
    return sequence.SerializeToString()

  return tf.py_func(jitter_label, [sequence_tensor], tf.string)


def truncate_note_sequence(sequence, truncate_secs):
  """Truncates a NoteSequence to the given length."""
  sus_sequence = sequences_lib.apply_sustain_control_changes(sequence)

  truncated_seq = music_pb2.NoteSequence()

  for note in sus_sequence.notes:
    start_time = note.start_time
    end_time = note.end_time

    if start_time > truncate_secs:
      continue

    if end_time > truncate_secs:
      end_time = truncate_secs

    modified_note = truncated_seq.notes.add()
    modified_note.MergeFrom(note)
    modified_note.start_time = start_time
    modified_note.end_time = end_time
  if truncated_seq.notes:
    truncated_seq.total_time = truncated_seq.notes[-1].end_time
  return truncated_seq


def truncate_note_sequence_op(sequence_tensor, truncated_length_frames,
                              hparams):
  """Truncates a NoteSequence to the given length."""
  def truncate(sequence_tensor, num_frames):
    sequence = music_pb2.NoteSequence.FromString(sequence_tensor)
    num_secs = num_frames / hparams_frames_per_second(hparams)
    return truncate_note_sequence(sequence, num_secs).SerializeToString()
  res = tf.py_func(
      truncate,
      [sequence_tensor, truncated_length_frames],
      tf.string)
  res.set_shape(())
  return res


InputTensors = collections.namedtuple(
    'InputTensors', ('spec', 'spectrogram_hash', 'labels', 'label_weights',
                     'length', 'onsets', 'offsets', 'velocities', 'sequence_id',
                     'note_sequence'))


def preprocess_data(sequence_id, sequence, audio, velocity_range, hparams,
                    is_training):
  """Compute spectral representation, labels, and length from sequence/audio.

  Args:
    sequence_id: id of the sequence.
    sequence: String tensor containing serialized NoteSequence proto.
    audio: String tensor containing containing WAV data.
    velocity_range: String tensor containing max and min velocities of file as a
      serialized VelocityRange.
    hparams: HParams object specifying hyperparameters.
    is_training: Whether or not this is a training run.

  Returns:
    An InputTensors tuple.

  Raises:
    ValueError: If hparams is contains an invalid spec_type.
  """

  wav_jitter_amount_ms = label_jitter_amount_ms = 0
  # if there is combined jitter, we must generate it once here
  if is_training and hparams.jitter_amount_ms > 0:
    wav_jitter_amount_ms = np.random.choice(hparams.jitter_amount_ms, size=1)
    label_jitter_amount_ms = wav_jitter_amount_ms

  if label_jitter_amount_ms > 0:
    sequence = jitter_label_op(sequence, label_jitter_amount_ms / 1000.)

  # possibly shift the entire sequence backward for better forward only training
  if hparams.backward_shift_amount_ms > 0:
    sequence = jitter_label_op(sequence,
                               hparams.backward_shift_amount_ms / 1000.)

  if is_training:
    audio = transform_wav_data_op(
        audio,
        hparams=hparams,
        jitter_amount_sec=wav_jitter_amount_ms / 1000.)

  if hparams.spec_type == 'tflite_compat_mel':
    assert hparams.spec_log_amplitude
    spec = tflite_compat_mel(audio, hparams=hparams)
  else:
    spec = wav_to_spec_op(audio, hparams=hparams)
  spectrogram_hash = get_spectrogram_hash_op(spec)

  labels, label_weights, onsets, offsets, velocities = sequence_to_pianoroll_op(
      sequence, velocity_range, hparams=hparams)

  length = wav_to_num_frames_op(audio, hparams_frames_per_second(hparams))

  asserts = []
  if hparams.max_expected_train_example_len and is_training:
    asserts.append(
        tf.assert_less_equal(length, hparams.max_expected_train_example_len))

  with tf.control_dependencies(asserts):
    return InputTensors(
        spec=spec,
        spectrogram_hash=spectrogram_hash,
        labels=labels,
        label_weights=label_weights,
        length=length,
        onsets=onsets,
        offsets=offsets,
        velocities=velocities,
        sequence_id=sequence_id,
        note_sequence=sequence)


FeatureTensors = collections.namedtuple(
    'FeatureTensors', ('spec', 'length', 'sequence_id'))
LabelTensors = collections.namedtuple(
    'LabelTensors', ('labels', 'label_weights', 'onsets', 'offsets',
                     'velocities', 'note_sequence', 'supervised', 'mix_ratios'))


def _provide_data(input_tensors, hparams, is_training, label_ratio=1.0):
  """Returns tensors for reading batches from provider."""
  length = tf.cast(input_tensors.length, tf.int32)
  labels = tf.reshape(input_tensors.labels, (-1, constants.MIDI_PITCHES))
  label_weights = tf.reshape(input_tensors.label_weights,
                             (-1, constants.MIDI_PITCHES))
  onsets = tf.reshape(input_tensors.onsets, (-1, constants.MIDI_PITCHES))
  offsets = tf.reshape(input_tensors.offsets, (-1, constants.MIDI_PITCHES))
  velocities = tf.reshape(input_tensors.velocities,
                          (-1, constants.MIDI_PITCHES))
  spec = tf.reshape(input_tensors.spec, (-1, hparams_frame_size(hparams)))

  # Determine whether to use datapoint labels from spectrogram hash.
  spectrogram_hash = tf.cast(input_tensors.spectrogram_hash, tf.int64)
  if label_ratio == 0:
    supervised = tf.cast(False, tf.bool)
  else:
    label_mod = int(1.0 / label_ratio)
    supervised = tf.logical_not(tf.cast(spectrogram_hash % label_mod, tf.bool))

  # Slice specs and labels tensors so they are no longer than truncated_length.
  hparams_truncated_length = tf.cast(
      hparams.truncated_length_secs * hparams_frames_per_second(hparams),
      tf.int32)
  if hparams.truncated_length_secs:
    truncated_length = tf.reduce_min([hparams_truncated_length, length])
  else:
    truncated_length = length

  if is_training:
    truncated_note_sequence = tf.constant(0)
  else:
    truncated_note_sequence = truncate_note_sequence_op(
        input_tensors.note_sequence, truncated_length, hparams)

  # If max_expected_train_example_len is set, ensure that all examples are
  # padded to this length. This results in a fixed shape that can work on TPUs.
  if hparams.max_expected_train_example_len and is_training:
    # In this case, final_length is a constant.
    if hparams.truncated_length_secs:
      assert_op = tf.assert_equal(hparams.max_expected_train_example_len,
                                  hparams_truncated_length)
      with tf.control_dependencies([assert_op]):
        final_length = hparams.max_expected_train_example_len
    else:
      final_length = hparams.max_expected_train_example_len
  else:
    # In this case, it is min(hparams.truncated_length, length)
    final_length = truncated_length

  spec_delta = tf.shape(spec)[0] - final_length
  spec = tf.case(
      [(spec_delta < 0,
        lambda: tf.pad(spec, tf.stack([(0, -spec_delta), (0, 0)]))),
       (spec_delta > 0, lambda: spec[0:-spec_delta])],
      default=lambda: spec)
  labels_delta = tf.shape(labels)[0] - final_length
  labels = tf.case(
      [(labels_delta < 0,
        lambda: tf.pad(labels, tf.stack([(0, -labels_delta), (0, 0)]))),
       (labels_delta > 0, lambda: labels[0:-labels_delta])],
      default=lambda: labels)
  label_weights = tf.case(
      [(labels_delta < 0,
        lambda: tf.pad(label_weights, tf.stack([(0, -labels_delta), (0, 0)]))
       ), (labels_delta > 0, lambda: label_weights[0:-labels_delta])],
      default=lambda: label_weights)
  onsets = tf.case(
      [(labels_delta < 0,
        lambda: tf.pad(onsets, tf.stack([(0, -labels_delta), (0, 0)]))),
       (labels_delta > 0, lambda: onsets[0:-labels_delta])],
      default=lambda: onsets)
  offsets = tf.case(
      [(labels_delta < 0,
        lambda: tf.pad(offsets, tf.stack([(0, -labels_delta), (0, 0)]))),
       (labels_delta > 0, lambda: offsets[0:-labels_delta])],
      default=lambda: offsets)
  velocities = tf.case(
      [(labels_delta < 0,
        lambda: tf.pad(velocities, tf.stack([(0, -labels_delta), (0, 0)]))),
       (labels_delta > 0, lambda: velocities[0:-labels_delta])],
      default=lambda: velocities)

  mix_ratios = tfp.distributions.Beta(hparams.mix_beta,
                                      hparams.mix_beta).sample(1)

  features = FeatureTensors(
      spec=tf.reshape(spec, (final_length, hparams_frame_size(hparams), 1)),
      length=truncated_length,
      sequence_id=tf.constant(0) if is_training else input_tensors.sequence_id)
  labels = LabelTensors(
      labels=tf.reshape(labels, (final_length, constants.MIDI_PITCHES)),
      label_weights=tf.reshape(label_weights,
                               (final_length, constants.MIDI_PITCHES)),
      onsets=tf.reshape(onsets, (final_length, constants.MIDI_PITCHES)),
      offsets=tf.reshape(offsets, (final_length, constants.MIDI_PITCHES)),
      velocities=tf.reshape(velocities, (final_length, constants.MIDI_PITCHES)),
      note_sequence=truncated_note_sequence,
      supervised=supervised,
      mix_ratios=mix_ratios)

  return features, labels


def _get_dataset(examples, preprocess_examples, hparams, is_training,
                 shuffle_examples, shuffle_buffer_size, skip_n_initial_records,
                 label_ratio=1.0):
  """Returns a tf.data.Dataset from TFRecord files.

  Args:
    examples: A string path to a TFRecord file of examples, a python list of
      serialized examples, or a Tensor placeholder for serialized examples.
    preprocess_examples: Whether to preprocess examples. If False, assume they
      have already been preprocessed.
    hparams: HParams object specifying hyperparameters.
    is_training: Whether this is a training run.
    shuffle_examples: Whether examples should be shuffled.
    shuffle_buffer_size: Buffer size used to shuffle records.
    skip_n_initial_records: Skip this many records at first.
    label_ratio: A float representing the proportion of data that should have
      labels. For example, 1.0 would be fully supervised training.

  Returns:
    A tf.data.Dataset.
  """
  if is_training and not shuffle_examples:
    raise ValueError('shuffle_examples must be True if is_training is True')

  if isinstance(examples, str):
    # Read examples from a TFRecord file containing serialized NoteSequence
    # and audio.
    filenames = tf.data.Dataset.list_files(examples, shuffle=shuffle_examples)
    if shuffle_examples:
      input_dataset = filenames.apply(
          tf.data.experimental.parallel_interleave(
              tf.data.TFRecordDataset, sloppy=True, cycle_length=8))
    else:
      input_dataset = tf.data.TFRecordDataset(filenames)
  else:
    input_dataset = tf.data.Dataset.from_tensor_slices(examples)

  if shuffle_examples:
    input_dataset = input_dataset.shuffle(shuffle_buffer_size)
  if is_training:
    input_dataset = input_dataset.repeat()
  if skip_n_initial_records:
    input_dataset = input_dataset.skip(skip_n_initial_records)

  def _preprocess(example_proto):
    """Process an Example proto into a model input."""
    features = {
        'id': tf.FixedLenFeature(shape=(), dtype=tf.string),
        'sequence': tf.FixedLenFeature(shape=(), dtype=tf.string),
        'audio': tf.FixedLenFeature(shape=(), dtype=tf.string),
        'velocity_range': tf.FixedLenFeature(shape=(), dtype=tf.string),
    }
    record = tf.parse_single_example(example_proto, features)
    input_tensors = preprocess_data(record['id'], record['sequence'],
                                    record['audio'], record['velocity_range'],
                                    hparams, is_training)
    return _provide_data(
        input_tensors,
        hparams=hparams,
        is_training=is_training,
        label_ratio=label_ratio)

  def _parse(example_proto):
    """Process an Example proto into a model input."""
    features = {
        'spec': tf.VarLenFeature(dtype=tf.float32),
        'spectrogram_hash': tf.FixedLenFeature(shape=(), dtype=tf.int64),
        'labels': tf.VarLenFeature(dtype=tf.float32),
        'label_weights': tf.VarLenFeature(dtype=tf.float32),
        'length': tf.FixedLenFeature(shape=(), dtype=tf.int64),
        'onsets': tf.VarLenFeature(dtype=tf.float32),
        'offsets': tf.VarLenFeature(dtype=tf.float32),
        'velocities': tf.VarLenFeature(dtype=tf.float32),
        'sequence_id': tf.FixedLenFeature(shape=(), dtype=tf.string),
        'note_sequence': tf.FixedLenFeature(shape=(), dtype=tf.string),
    }
    record = tf.parse_single_example(example_proto, features)
    input_tensors = InputTensors(
        spec=tf.sparse.to_dense(record['spec']),
        spectrogram_hash=record['spectrogram_hash'],
        labels=tf.sparse.to_dense(record['labels']),
        label_weights=tf.sparse.to_dense(record['label_weights']),
        length=record['length'],
        onsets=tf.sparse.to_dense(record['onsets']),
        offsets=tf.sparse.to_dense(record['offsets']),
        velocities=tf.sparse.to_dense(record['velocities']),
        sequence_id=record['sequence_id'],
        note_sequence=record['note_sequence'])
    return _provide_data(
        input_tensors,
        hparams=hparams,
        is_training=is_training,
        label_ratio=label_ratio)

  dataset = input_dataset.map(_preprocess if preprocess_examples else _parse)
  return dataset


def _batch(dataset, hparams, is_training, batch_size=None):
  """Batch a dataset, optional batch_size override."""
  if not batch_size:
    batch_size = hparams.batch_size
  if hparams.max_expected_train_example_len and is_training:
    dataset = dataset.batch(batch_size, drop_remainder=True)
  else:
    dataset = dataset.padded_batch(
        batch_size,
        padded_shapes=dataset.output_shapes,
        drop_remainder=True)
  return dataset


def provide_batch(examples,
                  preprocess_examples,
                  hparams,
                  is_training=True,
                  shuffle_examples=None,
                  shuffle_buffer_size=64,
                  skip_n_initial_records=0,
                  semisupervised_configs=None):
  """Returns batches of tensors read from TFRecord files.

  Args:
    examples: A string path to a TFRecord file of examples, a python list of
      serialized examples, or a Tensor placeholder for serialized examples.
    preprocess_examples: Whether to preprocess examples. If False, assume they
      have already been preprocessed.
    hparams: HParams object specifying hyperparameters.
      is_training: Whether this is a training run.
    shuffle_examples: Whether examples should be shuffled. If not set, will
      default to the value of is_training.
    shuffle_buffer_size: Buffer size used to shuffle records.
    skip_n_initial_records: Skip this many records at first.
    semisupervised_configs: A list of SemisupervisedExamplesConfig that gives
      datasets for semisupervised training. Overrides examples.

  Returns:
    Batched tensors in a TranscriptionData NamedTuple.
  """
  def _examples_is_valid():
    return isinstance(examples, tf.Tensor) or examples
  if not _examples_is_valid() and not semisupervised_configs:
    raise ValueError('You must provide `examples` or `semisupervised_configs`.')
  if _examples_is_valid() and semisupervised_configs:
    raise ValueError(
        'You must provide either `examples` or `semisupervised_configs`.')

  if shuffle_examples is None:
    shuffle_examples = is_training

  if not semisupervised_configs:
    # Just a single dataset.
    dataset = _get_dataset(
        examples, preprocess_examples=preprocess_examples, hparams=hparams,
        is_training=is_training, shuffle_examples=shuffle_examples,
        shuffle_buffer_size=shuffle_buffer_size,
        skip_n_initial_records=skip_n_initial_records)
    dataset = _batch(dataset, hparams, is_training)
  else:
    # Multiple datasets.
    datasets = []
    batch_ratios = []
    for ex in semisupervised_configs:
      dataset = _get_dataset(
          ex.examples_path, preprocess_examples=preprocess_examples,
          hparams=hparams, is_training=is_training,
          shuffle_examples=shuffle_examples,
          shuffle_buffer_size=shuffle_buffer_size,
          skip_n_initial_records=skip_n_initial_records,
          label_ratio=ex.label_ratio)
      datasets.append(dataset)
      batch_ratios.append(ex.batch_ratio)

    if hparams.semisupervised_concat:
      # Create a single batch by concatentating dataset batches.
      n_datasets = len(datasets)
      batch_size = hparams.batch_size // n_datasets
      # First create small batches.
      datasets = [_batch(d, hparams, is_training, batch_size) for d in datasets]
      dataset = tf.data.Dataset.zip(tuple(datasets))

      def _merge_datasets(*dataset_tuples):
        """Unzip and repack."""
        # Access __dict__ because can't convert namedtuple directly to a dict.
        features = [f.__dict__ for (f, _) in dataset_tuples]
        labels = [l.__dict__ for (_, l) in dataset_tuples]
        merged_features = {}
        for key in features[0].keys():
          merged_features[key] = tf.concat([f[key] for f in features], axis=0)
        merged_labels = {}
        for key in labels[0].keys():
          merged_labels[key] = tf.concat([f[key] for f in labels], axis=0)
        return FeatureTensors(**merged_features), LabelTensors(**merged_labels)

      # Then combine them.
      dataset = dataset.map(_merge_datasets)

    else:
      # Create a single batch by randomly sampling from the datasets.
      dataset = tf.data.experimental.sample_from_datasets(datasets,
                                                          weights=batch_ratios)
      dataset = _batch(dataset, hparams, is_training)

  dataset = dataset.prefetch(buffer_size=tf.data.experimental.AUTOTUNE)
  return dataset
