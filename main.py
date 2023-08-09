import sys
from libs import functionality_module as fm
from libs import read_write as rw


try:
    option = fm.init_menu()
    while True:

        if option == 's':
            option_1 = fm.menu()
            if option_1 == 'r':
                account = fm.create_userdata('r')
            elif option_1 == 'm':
                account = fm.create_userdata('m')
            else:
                print('Not a valid input, please try again!\n')
                continue
            fm.save_account (account)
            print(f'For the app: {account[0]} account info was stored in userdata')
            option = fm.init_menu()

        elif option == 'g':
            print('Type the app for which you want to get the user data')
            app_name = input("App: ").lower()
            print(f'For {app_name} the acount details are: \n{fm.get_userdata(app_name)}')
            option = fm.init_menu()
            continue
        elif option == 'e':
            sys.exit()
        else:
            print("Not a valid option")
            option = fm.init_menu()
            continue
except Exception as e:
    print(f'Something happened in main: {e}')
    option = fm.init_menu()

