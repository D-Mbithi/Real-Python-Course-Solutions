import os

path = '/home/dennis/Desktop/All/Real Python Course/book1/chp09/practice_files/images'

files = os.listdir(path)

for file in files:
    if os.path.isfile(os.path.join(path, file)):
        print(os.path.join(path, file))
