import os

my_path = '/home/dennis/Desktop/All/Real Python Course/book1/chp09/practice_files/images'

files_and_folders = os.listdir(my_path)

for folder_name in files_and_folders:
    full_path = os.path.join(my_path, folder_name)

    if os.path.isdir(full_path):
        os.rename(full_path, full_path+'_folder')

