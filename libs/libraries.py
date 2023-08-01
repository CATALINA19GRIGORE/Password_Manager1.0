"""
This module is used to save passwords and put them into a file
"""
from libs import read_write
import string
import random

def init_menu():
    print(f'Save password [s]\nExit [e]')
    return input('Your choice: ')


def menu():
    print(f'Random generated password [r]\nManually generated password [m]')
    return input('Choose wisely: ')


def save_password(path_to_file:str, app:str, passwd:str) -> None:
    """
    Saves data to database(csv file)

    :param path_to_file:The path to the file where we want to save the data
    :param app: String used to name an app
    :param passwd: String used as password
    :return: None
    """
    lst_app_pass = [app, passwd]
    read_write.append_to_file(path_to_file, lst_app_pass )


def random_pass():
    """
    Generates a string with random characters from a string containing letters, digits, punctuation and character space
    :return: a string of 12 random characters
    """
    characters = string.ascii_letters + string.digits + string.punctuation + ' '
    password = ''.join(random.choice(characters) for i in range(12))
    return password


if __name__ == '__main__':
    # save_password('D:\Gabriel\Curs_Python\Password Manager\passwords.csv', 'test_app', 'test_pass')
    pass