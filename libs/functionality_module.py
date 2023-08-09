"""This module is used to generate passwords and save them to database(csv file)


Functions:


init_menu(): Prompts user for input
menu(): Prompts user for input
get_password():  Finds a password based on the app given
save_password(): Saves data(password) to database(csv file)
random_pass_generator(): Generates a string of 12 random characters
"""

import os
from libs import read_write
import string
import random
# pathlib module to work with paths
from pathlib import Path


def init_menu():
    """
    Promts user for input
    :return: User input
    """
    if not os.path.exists(fr'{Path(__file__).parent.parent}\\userdata.csv'):
        read_write.create_file()
    print(f'Save password [s]\nGet Password [g]\nExit [e]')
    return input('Your choice: ')


def menu():
    """
    Prompts user for input
    :return: User input
    """
    print(f'Random generated password [r]\nManually generated password [m]')
    return input('Choose wisely: ')


def get_userdata(app_name):
    """
    Finds a password in the database based on the account given
    :param app_name: Application saved in database(input)
    """
    try:
        file = read_write.read_file(fr'{Path(__file__).parent.parent}\\userdata.csv', app_name)
        return f'Username:{file[1]}\nPassword:{file[2]}\nEmail:{file[3]}'

    except FileNotFoundError as e:
        read_write.create_file()
        print('userdata.csv created, please try again!')


def save_account(account: list) -> None:
    """
    Saves data to database(csv file)

    :param account: A list that will be saved in the database(csv file)

    :return: None
    """
    try:
        read_write.append_to_file(fr'{Path(__file__).parent.parent}\\userdata.csv', account)
    except FileNotFoundError as e:
        read_write.create_file()
        print('userdata.csv created, please try again!')


def random_pass_generator() -> str:
    """
    Generates a string with random characters from a string containing 6 letters, 4 digits and 2 punctuation characters
    :return: a string of 12 random characters
    """
    try:
        password = random.sample(string.ascii_letters, 6) + random.sample(string.digits, 4) \
                   + random.sample(string.punctuation, 2)
        random.shuffle(password)
        return ''.join(password)
    except Exception as e:
        print(f'Unexpected error: {e}')


def create_userdata(option: str) -> list:
    """
    Prompts user for input
    :param option: A string used for condition
    :return: Return a list of user input
    """
    if option == 'r':
        app = input('Enter App Name: ').lower()
        password = random_pass_generator()
        username = input('Type your username: ')
        email = input("Type your email address: ")
    else:
        app = input('Enter App Name: ').lower()
        password = input("Type the password")
        username = input('Type your username: ')
        email = input("Type your email address: ")

        print()
    return [app, username, password, email]


if __name__ == '__main__':
    print(random_pass_generator())
    print(os.path.exists(fr'{Path(__file__).parent.parent}\\userdata.csv'))


