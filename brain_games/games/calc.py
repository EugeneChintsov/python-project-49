"""This module describes the logic of the game brain-calc."""
from random import randint, choice
from operator import add, sub, mul


MIN_NUMBER = -10
MAX_NUMBER = 10
DESCRIPTION = 'What is the result of the expression?'


def calculate(operator: str, num1: int, num2: int) -> int:
    """Apply operator for two numbers and return result"""
    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = sub(num1, num2)
    elif operator == '*':
        result = mul(num1, num2)
    return result


def get_parametres() -> tuple[str, str]:
    """Release game logic and return parameters for game engine"""
    operator = choice('+-*')
    number1 = randint(MIN_NUMBER, MAX_NUMBER)
    number2 = randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = str(calculate(operator, number1, number2))
    question = f'{number1} {operator} {number2}'
    return question, correct_answer
