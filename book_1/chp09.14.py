import os

path = '/home/dennis/Desktop/All/Real Python Course/book1/chp09/practice_files/images'

file_paths = os.listdir(path)

for file in file_paths:
    print(os.path.join(path, file))
