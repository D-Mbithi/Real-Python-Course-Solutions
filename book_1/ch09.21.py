import os
import csv

my_path = '/home/dennis/Desktop/All/Real Python Course/book1/chp09/practice_files'

with open(os.path.join(my_path, 'movies.csv'), 'w') as movies:
    movies_writer = csv.writer(movies)

    movies_writer.writerow(['Movie','Rating'])
    movies_writer.writerow(['Rebel without a Cuse','3'])
    movies_writer.writerow(['Monty Python\'s life of Brian','5'])
    movies_writer.writerow(['Santa claus conquers the Martians','0'])
