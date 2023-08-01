import sys
from libs import libraries



option = libs.init_menu()
while True:
    if option == 's':
        app = input('Enter App Name: ')
        option_1 = menu()
        if option_1 == 'r':
            password = libraries.random_pass()
        else:
            password = input('Type your password:')
        

        libs.save_password('./passwords.csv', app, password)
