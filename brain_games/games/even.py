"""This module describes the logic of the game brain-even."""
from random import randint


MIN_NUMBER = -10
MAX_NUMBER = 10
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num: int) -> bool:
    """Determines whether a number is even and returns the answer."""
    return True if num % 2 == 0 else False


def generate_game() -> tuple[str, str]:
    """Release game logic and return parameters for game engine"""
    number = randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = 'no'
    if is_even(number):
        correct_answer = 'yes'
    question = str(number)
    return question, correct_answer
