"""
This module is used to save passwords and put them into a file
"""
from libs import read_write
import string
import random


def init_menu():
    print(f'Save password [s]\nGet Password [g]\nExit [e]')
    return input('Your choice: ')


def menu():
    print(f'Random generated password [r]\nManually generated password [m]')
    return input('Choose wisely: ')


def get_password(user_account):
    """
    Finds a password based on the account given
    :param user_account: Account in the database
    """
    file = read_write.read_file('D:\Gabriel\Curs_Python\Password Manager\passwords.csv')
    for row in file:
        if row[0] == user_account:
            return row[1]

    else:
        print(f'This account doesnt exist in the file')


def save_password(path_to_file: str, app: str, passwd: str) -> None:
    """
    Saves data to database(csv file)

    :param path_to_file:The path to the file where we want to save the data
    :param app: String used to name an app
    :param passwd: String used as password
    :return: None
    """
    lst_app_pass = [app, passwd]
    read_write.append_to_file(path_to_file, lst_app_pass)


def random_pass_generator():
    """
    Generates a string with random characters from a string containing 6 letters, 4 digits and 2 punctuation characters
    :return: a string of 12 random characters
    """
    pass_letters = ''.join(random.choice(string.ascii_letters) for _ in range(6))
    pass_digits = ''.join(random.choice(string.digits) for _ in range(4))
    pass_punctuation = ''.join(random.choice(string.punctuation) for _ in range(2))
    password = ''.join(set(pass_letters + pass_digits + pass_punctuation))
    return password


# if __name__ == '__main__':
#     print(random_pass())
