import random

characters = 'q w e r t y u i o p a s d f g h j k l z x c v b n m Q W E R T Y U I O P A S D F G H J K L Z X C V B N M ! @ # $ % & / ( ) = ?'

#Could work better
#Cause the password depends on the position of the characters

characters = characters.split(' ')

def generate_password(number_characters):
    password = ''
    for i in range(number_characters):
        num = random.randint(0, 36)
        password+=characters[num]
    return password

def add_newPassword(password_location,password):
    file = open('passwords.txt', 'a')
    file.write(password_location+','+password+'\n')
    file.close()

def show_passwords():
    file = open('passwords.txt', 'r')
    content = file.read()
    return print(content)