import os

path = '/home/dennis/Desktop/All/Real Python Course/book1/chp09/practice_files/images'

for root, dirs, files in os.walk(path):
    for file in files:
        full_file_path = os.path.join(root, file)

        if os.path.getsize(full_file_path) < 2000:
            if full_file_path.endswith('.jpg'):
                print(file, 'will be deleted')
                os.remove(full_file_path)
        else:
            print(file, 'wun\'t be deleted')

