import os

# Opens Login & Sign In Page
def Access():
    print('Welcome User')
    print('1. Login\n2. Sign In\n3. Exit')

    option = int(input('\nChoose an option: '))
    while option != 1 or option !=2 or option !=3:
        print('\nOPTION NOT VALID')
        option = int(input('Choose an option: '))


# User sign in info
def Sign_In():
    pass


# User login info
def Login():
    pass


# Checks user login info
def Login_Check():
    pass


# Clear CMD
def Clear():
    os.system('cls')


# Run the program
if __name__ == "__main__":
    Access()