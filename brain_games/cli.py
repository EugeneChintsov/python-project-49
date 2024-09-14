import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    User_Name = prompt.string('May I have your name? \n')
    print(f'Hello,{User_Name}!')
    return User_Name
