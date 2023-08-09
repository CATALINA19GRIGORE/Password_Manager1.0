"""Used for:
1. Read from file
2. Write to file
"""
import csv
import os.path
from pathlib import Path


def create_file() -> None:
    """Creates a csv file using dictionary"""
    try:
        with open('../userdata.csv', 'w', newline='') as csvfile:
            cap_tabel = ['App Name', 'Username', 'Password', 'Email']
            writer = csv.DictWriter(csvfile, fieldnames=cap_tabel)
            writer.writeheader()

    except Exception as e:
        print(f'Something happened in create_file: {e}')


def read_file(path_to_file, app_name):
    """
    Opens a csv file and reads its content
    :param path_to_file: The path to the csv file
    :param app_name:
    :return:Content of the file as a list
    """
    try:
        with open(path_to_file,'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['App Name'] != app_name:
                    continue
                return [row['App Name'], row['Username'], row['Password'], row['Email']]
    except Exception as e:
        print(f'read_file problem:{e}')


def append_to_file(path_to_file, lst):
    """
    Appends a row to a csv file
    :param path_to_file: The path to the file where we want to append the dataa
    :param lst: A list containing the data we want to append in a row in the csv file
    :return: None
    """
    try:
        with open(path_to_file, 'a', newline='') as csvfile:
            cap_tabel = ['App Name', 'Username', 'Password', 'Email']
            writer = csv.DictWriter(csvfile, fieldnames=cap_tabel)
            writer.writerow({'App Name': lst[0], 'Username': lst[1], 'Password': lst[2], 'Email': lst[3]})
    except Exception as e:
        print(f'Something happened in append_file: {e}')


if __name__ == '__main__':
    # create_file()
    # read_file(fr'{Path(__file__).parent.parent}\\userdata.csv', 'git')
    append_to_file(fr'{Path(__file__).parent.parent}\\userdata.csv', ['testapp', 'testuser', 'testpass', 'testmail'])
