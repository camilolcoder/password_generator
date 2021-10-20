import os
import random
import pandas as pd

characters = 'q w e r t y u i o p a s d f g h j k l z x c v b n m Q W E R T Y U I O P A S D F G H J K L Z X C V B N M ! @ # $ % & / ( ) = ? 0 1 2 3 4 5 6 7 8 9'

#Could work better
#Cause the password depends on the position of the characters
letters = 'q w e r t y u i o p a s d f g h j k l z x c v b n m'
capital_letters = 'Q W E R T Y U I O P A S D F G H J K L Z X C V B N M'
numbers = '0 1 2 3 4 5 6 7 8 9'
special_characters = '! @ # $ % & / ( ) = ?'

characters = characters.split(' ')

def generate_password(number_characters):
    password = ''
    for i in range(number_characters):
        num = random.randint(0, 36)
        password+=characters[num]
    return password

def select_random_character(characters_list):
        return characters_list[random.randint(0, len(characters_list))-1]

#This one is an improved version of the function generate_password
#the actual reason why this one is better is because some websites
#ask for a minimun capital letter, this version at least have a 
#capital letter
def generate_password2(number_character):
    password = [0]*number_character
    pos = random.randint(0,len(password)-1)
    password[pos] = select_random_character(capital_letters)
    for i in range(len(password)):
        if password != 0:
            password[i] = select_random_character(characters)
    password = ''.join(password)
    return password
        
def check_file():
    check = os.path.exists('./passwords.txt')
    return check        
#print(check_file())

def add_newPassword(password_location,password):
    file = open('passwords.txt', 'a')
    # if not check_file():
    #     file.write('domain, '+'password'+'\n')
    file.write(password_location+','+password+'\n')
    file.close()

def show_passwords():
    df = pd.read_csv('passwords.txt', sep=',', header=None)
    df.columns = ['Domains', 'Passwords']
    print(df)
    # file = open('passwords.txt', 'r')
    # content = file.read()
    # return print(content)

def find_password(domain):
    print('Working on this option')