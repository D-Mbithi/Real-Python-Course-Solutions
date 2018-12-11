import os

my_path = '/home/dennis/Desktop/All/Real Python Course/book1/chp09/practice_files/images'

# get a list of files in the folder
filename_list = os.listdir(my_path)

# print(filename_list)

# loop through every file in the main folder
for filename in filename_list:
    if filename.lower().endswith('.gif'):
        print("Converting {} to JPG".format(filename))

        full_file_name = os.path.join(my_path, filename)

        new_file_name = full_file_name[:-4] + '.jpg'

        print(new_file_name)

        os.rename(full_file_name, new_file_name)
