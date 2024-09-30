"""This module describes the logic of the game brain-gcd."""
from random import randint


MIN_NUMBER = -10
MAX_NUMBER = 10
DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def find_gcd(number1: int, number2: int) -> int:
    """Determines the greatest common divisor of two numbers."""
    return number1 if number2 == 0 else find_gcd(number2, number1 % number2)


def generate_game() -> tuple[str, str]:
    """Release game logic and return parameters for game engine"""
    number1 = randint(MIN_NUMBER, MAX_NUMBER)
    number2 = randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = str(abs(find_gcd(number1, number2)))
    question = f'{number1} {number2}'
    return question, correct_answer
