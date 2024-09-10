import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have yout name? \n')
    print(f'Hello,{name}!')
