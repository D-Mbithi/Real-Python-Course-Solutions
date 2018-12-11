import os
import glob


path = '/home/dennis/Desktop/All/Real Python Course/book1/chp09/practice_files/images'

file_path = os.path.join(path, "*.png")

for file in glob.glob(file_path):
    print(os.path.join(path, file))
