"""This module describes the logic of the game brain-even."""
from random import randint


MIN_NUMBER = -10
MAX_NUMBER = 10
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number: int) -> str:
    """Determines whether a number is even and returns the answer."""
    return 'yes' if number % 2 == 0 else 'no'


def generate_game() -> tuple[str, str]:
    """Release game logic and return parameters for game engine"""
    number = randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = is_even(number)
    question = str(number)
    return question, correct_answer
