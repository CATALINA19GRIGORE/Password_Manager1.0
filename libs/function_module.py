"""This module is used to generate passwords and save them to database(csv file)


Functions:


init_menu(): Prompts user for input
menu(): Prompts user for input
get_password():  Finds a password based on the app given
save_password(): Saves data(password) to database(csv file)
random_pass_generator(): Generates a string of 12 random characters
"""


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
        file = read_write.read_file(fr'{Path(__file__).parent.parent}\\userdata.csv')
        for row in file:
            if row[0] == app_name:
                return f'Password:{row[1]}\nUsername:{row[2]}\nEmail:{row[3]}'

        else:
            print(f'This account doesnt exist in the file')
    except FileNotFoundError as e:
        print(f'An error has occurred!: {e}')


def save_account(path_to_file: str, app: str, username: str,  passwd: str, email: str) -> None:
    """

    Saves data to database(csv file)

    :param path_to_file:The path to the file where we want to save the data
    :param app: String used to name an app
    :param username: String used as username
    :param passwd: String used as password
    :param email: String used for email address
    :return: None
    """
    try:
        lst_app_pass = [app, username, passwd, email]
        read_write.append_to_file(path_to_file, lst_app_pass)
    except Exception as e:
        print(e)


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


if __name__ == '__main__':
    print(random_pass_generator())
    save_account()