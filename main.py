import csv
import sys
from libs import function_module as fm



option = fm.init_menu()
while True:
    try:
        if option == 's':
            app = input('Enter App Name: ').lower()
            option_1 = fm.menu()
            if option_1 == 'r':
                password = fm.random_pass_generator()
                username = input('Type your username: ')
                email = input("Type your email address: ")
            else:
                password = input('Type your password:')
                username = input('Type your username: ')
                email = input("Type your email address: ")
            fm.save_account('./userdata.csv', app, password, username, email)
            print(f'For the app: {app} \npassword: {password} has been allocated')
            option = fm.init_menu()
        elif option == 'g':
            print('Type the account for which you want to get the password')
            app_name = input("App: ").lower()
            print(f'For {app_name} the acount details are: {fm.get_password(app_name)}')
            option = fm.init_menu()
        elif option == 'e':
            sys.exit()
        else:
            print("Not a valid option")
            option = fm.init_menu()
    except FileNotFoundError as e:
        with open('userdata.csv', 'w', newline='') as file_w:
            writer = csv.writer(file_w)
            writer.writerow(['App', 'Username', 'Password', 'Email'])
        option = fm.init_menu()
