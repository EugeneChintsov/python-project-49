"""This module describes the logic of the game brain-calc."""
from random import randint, choice
from operator import add, sub, mul


MIN_NUMBER = -10
MAX_NUMBER = 10
OPERATORS = ('+-*')
DESCRIPTION = 'What is the result of the expression?'


def calculate(operator: str, number1: int, number2: int) -> int:
    """Apply operator for two numbers and return result"""
    if operator == '+':
        result = add(number1, number2)
    elif operator == '-':
        result = sub(number1, number2)
    elif operator == '*':
        result = mul(number1, number2)
    return result


def generate_game() -> tuple[str, str]:
    """Release game logic and return parameters for game engine"""
    operator = choice(OPERATORS)
    number1 = randint(MIN_NUMBER, MAX_NUMBER)
    number2 = randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = str(calculate(operator, number1, number2))
    question = f'{number1} {operator} {number2}'
    return question, correct_answer
