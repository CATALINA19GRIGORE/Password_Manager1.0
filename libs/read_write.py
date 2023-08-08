"""Used for:
1. Read from file
2. Write to file
"""
import csv


def read_file(path_to_file):
    """
    Opens a csv file and reads its content
    :param path_to_file: The path to the csv file
    :return:Content of the file as a list
    """
    try:
        with open(path_to_file, 'r', newline='') as file_r:
            content = csv.reader(file_r)
            return list(content)

    except FileNotFoundError as e:
        print('File has been created, now you can register new data')
        with open('userdata.csv', 'w') as file_w:
            writer = csv.writer(file_w)
            writer.writerow(['App', 'Username', 'Password', 'Email'])
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
        with open(path_to_file, 'a', newline='') as file_a:
            writer = csv.writer(file_a)
            writer.writerow(lst)

    except FileNotFoundError as e:
        print('File userdata.csv created')
        with open('userdata.csv', 'w') as file_w:
            writer = csv.writer(file_w)
            writer.writerow(['App', 'Username', 'Password', 'Email'])



if __name__ == '__main__':
    pass