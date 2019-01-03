# Script to split single CSV file multiple files

import os
import csv
import argparse

# add function for commandline arguments parsed.
path = '/home/dennis/Desktop/All/Real Python Course/book1/chp09/practice_files'
current_path = os.getcwd()


def get_commandline_arguements():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', nargs=1, help='Gets the input file details')
    parser.add_argument('-o', nargs=1, help='Gets the output file details')
    parser.add_argument(
            '-r', nargs=1, type=int,
            help='Gets the number of rows per split in the output files'
            )
    args = parser.parse_args()

    return args.i[0], args.o[0], args.r[0]


def check_csv_file_isvalid():
    input_file, output_file, rows = get_commandline_arguements()

    if os.path.exists(os.path.join(current_path, input_file)):
        return True
    else:
        return False


def check_number_of_rows_in_csv():
    if not check_csv_file_isvalid:
        print("There is nos inputfile available")

    input_file, output_file, rows = get_commandline_arguements()

    with open(os.path.join(current_path, input_file), 'r') as csv_input:
        csv_reader = csv.reader(csv_input)

        if len(list(csv_reader)) > rows:
            return True
        else:
            return False

def split_rows():
    if check_number_of_rows_in_csv:
        input_file, output_file, rows = get_commandline_arguements()

    with open(os.path.join(current_path, input_file), 'r') as csv_data:
        csv_reader = csv.reader(csv_data)
        next(csv_reader)
        csv_list = list(csv_reader)

        if len(csv_list) % rows == 0:
            number_of_files = len(csv_list) // rows
        else:
            number_of_files = len(csv_list) // rows + 1

    count = 0
    rows_dict = {}

    for num in range(number_of_files):
        row_list = csv_list[count:count+rows]
        name = output_file+'_'+str(num+1)+'.csv'
        rows_dict[name] = row_list
        count += rows

    for each_name, each_list in rows_dict.items():
        with open(os.path.join(os.path.join(current_path, 'output'), each_name), 'w') as csv_file:
            csv_writer = csv.writer(csv_file)

            for line in each_list:
                csv_writer.writerow(line)


if __name__ == '__main__':
    split_rows()

