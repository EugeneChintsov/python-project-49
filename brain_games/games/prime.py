"""This module describes the logic of the game brain-prime."""
from random import randint


MIN_NUMBER = 0
MAX_NUMBER = 10
FIRST_DIVIDER = 2
DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number: int) -> bool:
    """Determines whether a number is prime and returns the answer."""
    if number < FIRST_DIVIDER:
        return False
    middle_divider = int(number ** 0.5) + 1
    for i in range(FIRST_DIVIDER, middle_divider):
        if number % i == 0:
            return False
    return True


def generate_game() -> tuple[str, str]:
    """Release game logic and return parameters for game engine"""
    number = randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = 'yes' if is_prime(number) else 'no'
    question = str(number)
    return question, correct_answer
