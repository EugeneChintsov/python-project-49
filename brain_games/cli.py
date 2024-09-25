"""This module describes the logic of command line interface."""
import prompt


def welcome_user():
    '''Read username and print greetings'''
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? \n')
    print(f'Hello, {username}!')
