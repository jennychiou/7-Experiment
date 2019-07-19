from os import walk
from os.path import join
import os
import click
import sys

def file_path(base_path,Deputy_file_name):
    folder_list = []
    file_list = []
    file_name = []
    folder_name = []

    for root, dirs, files in walk(base_path):

        for f in files:
            file_path = join(root, f)
                
            if file_path.endswith(Deputy_file_name):
                file_name.append(os.path.splitext(f)[0])
                file_list.append(file_path)
        
        for folder in dirs:
            folder_path = join(root, folder)
            folder_list.append(folder_path)
            folder_name.append(folder)

    return file_list, file_name, folder_list, folder_name