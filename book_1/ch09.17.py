import os

path = '/home/dennis/Desktop/All/Real Python Course/book1/chp09/practice_files/images'

files_path = os.listdir(path)

for root,dirs,files in os.walk(path):
    for file in files:
        if file.endswith('.png'):
            full_file_path = os.path.join(root, file)

            os.rename(full_file_path, full_file_path[:-4]+'.jpg')

        print(os.path.join(root, file))
