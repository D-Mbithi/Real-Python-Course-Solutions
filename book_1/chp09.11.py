import os
import glob

my_path = '/home/dennis/Desktop/All/Real Python Course/book1/chp09/practice_files/images'

possible_files = os.path.join(my_path, '*/*.png')

for file_name in glob.glob(possible_files):
    print(file_name)
