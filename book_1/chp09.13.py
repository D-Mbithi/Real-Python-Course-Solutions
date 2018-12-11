import os

my_path = '/home/dennis/Desktop/All/Real Python Course/book1/chp09/practice_files/images'


for current_folder, subfolders, file_names in os.walk(my_path):
    for file_name in file_names:
        print(os.path.join(current_folder, file_name))

