import sys 
import password_manager as pm

def printMenu():
    print('')
    print('1. Generate a new password')
    print('2. Search a password')
    print('3. Show all the passwords')
    print('4. Exit program')

def main():
    while True:
        printMenu()
        option = input('Type the number of the option you want to use: ')
        print('')
        if option == '1':
            try:
                site = input('Type the name of the site the password is being made for: ')
                number_characters = int(input('Type a number, this will be the len of your password: '))
                new_password = pm.generate_password2(number_characters)
                pm.add_newPassword(site, new_password)
                print('This is your new password: '+new_password)
            except:
                print('Please type a valid number')
        elif option == '2':
            print('Working on it')
        elif option == '3':
            pm.show_passwords()
        else:
            sys.exit(0)

if __name__ == '__main__':
    main()