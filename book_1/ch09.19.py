import os
import csv

my_path = '/home/dennis/Desktop/All/Real Python Course/book1/chp09/practice_files'

with open(os.path.join(my_path, 'wonka.csv'), 'r') as my_file:
    my_file_reader = csv.reader(my_file)
    next(my_file_reader)

    for first_name, last_name, reward in my_file_reader:
        print("{} {} got: {}".format(first_name, last_name, reward))
