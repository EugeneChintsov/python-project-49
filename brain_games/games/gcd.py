"""This module describes the logic of the game brain-gcd."""
from random import randint


MIN_NUMBER = -10
MAX_NUMBER = 10
DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd(num1: int, num2: int) -> int:
    """Determines the greatest common divisor of two numbers."""
    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1 % num2)


def get_parametres() -> tuple[str, str]:
    """Release game logic and return parameters for game engine"""
    number1 = randint(MIN_NUMBER, MAX_NUMBER)
    number2 = randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = str(abs(gcd(number1, number2)))
    question = f'{number1} and {number2}'
    return question, correct_answer
