import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? \n')
    print(f'Hello,{username}!')
