import os
import csv

path = '/home/dennis/Desktop/All/Real Python Course/book1/chp09/practice_files'

with open(os.path.join(path, 'pastimes.csv'), 'r') as my_file, open(os.path.join(path, 'output/categorised output.cvs'), 'w') as output:
    my_file_reader = csv.reader(my_file)
    output_writer = csv.writer(output)
    next(my_file_reader)
    output_writer.writerow(['Person', 'Favourite Pasttime', 'Type of Pasttime'])


    for row in my_file_reader:
        if row[-1].lower().find('fighting') != -1:
            row.append('Combat')
        else:
            row.append('Other')

        output_writer.writerow(row)
