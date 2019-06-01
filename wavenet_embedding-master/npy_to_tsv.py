import io
import numpy as np
from file_load import file_path

file_list, file_names, folder_list, folder_name = file_path('./test', 'npy')
out_v = io.open('vecs.tsv', 'w', encoding='utf-8')
out_m = io.open('meta.tsv', 'w', encoding='utf-8')

for npy, name in zip(file_list,file_names):
    vec = np.load(npy)
    out_v.write('\t'.join([str(x) for x in vec]) + "\n")
    out_m.write(name.replace('.npy', '') + "\n")
    
# file_list, file_names, folder_list, folder_name = file_path('./dataset', '_OK.npy')

# for npy, name in zip(file_list,file_names):
#     vec = np.load(npy)
#     out_v.write('\t'.join([str(x) for x in vec]) + "\n")
#     out_m.write(name.replace('_0_OK', '') + "\n")

print("=====OK=====")

out_v.close()
out_m.close()
    