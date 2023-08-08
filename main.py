import csv
import sys
from libs import functionality_module as fm



option = fm.init_menu()
while True:
    try:
        if option == 's':
            option_1 = fm.menu()
            if option_1 == 'r':
                account = fm.create_userdata('r')
            else:
                account = fm.create_userdata('m')
            fm.save_account('./userdata.csv', account)
            print(f'For the app: {account[0]} account info was stored in userdata')
            option = fm.init_menu()
        elif option == 'g':
            print('Type the app for which you want to get the user data')
            app_name = input("App: ").lower()
            print(f'For {app_name} the acount details are: \n{fm.get_userdata(app_name)}')
            option = fm.init_menu()
        elif option == 'e':
            sys.exit()
        else:
            print("Not a valid option")
            option = fm.init_menu()
    except Exception as e:
        print(e)
        option = fm.init_menu()
