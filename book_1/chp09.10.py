import os
import glob

my_path = '/home/dennis/Desktop/All/Real Python Course/book1/chp09/practice_files/images'

possible_files = os.path.join(my_path, '*.gif')

for file_name in glob.glob(possible_files):
    print('Converting {} to JPG.....'.format(file_name))

    full_file_name = os.path.join(my_path, file_name)

    new_file_name = full_file_name[:-4]+'.jpg'

    os.rename(full_file_name, new_file_name)
