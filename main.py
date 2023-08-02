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
            else:
                password = input('Type your password:')
            fm.save_password('./passwords.csv', app, password)
            print(f'For the app: {app} \npassword: {password} has been allocated')
            break
        elif option == 'g':
            print('Type the account for which you want to get the password')
            user_account = input("Account: ").lower()
            print(f'For {user_account} the password is: {fm.get_password(user_account)}')
            option = fm.init_menu()
        elif option == 'e':
            sys.exit()
    except Exception as e:
        print(e)
