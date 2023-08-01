import sys
from libs import function_module as fm



option = libraries.init_menu()
while True:
    try:
        if option == 's':
            app = input('Enter App Name: ')
            option_1 = fm.menu()
            if option_1 == 'r':
                password = fm.random_pass_generator()
            else:
                password = input('Type your password:')
            libraries.save_password('./passwords.csv', app, password)
            print(f'For the app: {app} \npassword: {password} has been alocated')
            break

        else:
            sys.exit()
    except Exception as e:
        print(e)