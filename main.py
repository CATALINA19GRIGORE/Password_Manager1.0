import sys
from libs import libraries



option = libraries.init_menu()
while True:
    try:
        if option == 's':
            app = input('Enter App Name: ')
            option_1 = libraries.menu()
            if option_1 == 'r':
                password = libraries.random_pass()
            else:
                password = input('Type your password:')
            libraries.save_password('./passwords.csv', app, password)
            print(f'For the app: {app} \npassword: {password} has been alocated')
            break

        else:
            sys.exit()
    except Exception as e:
        print(e)