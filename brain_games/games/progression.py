"""This module describes the logic of the game brain-progression."""
from random import randint


MIN_NUMBER = -10
MAX_NUMBER = 10
MIN_STEP = 1
MAX_STEP = 10
MIN_LENGTH = 5
MAX_LENGTH = 10
DESCRIPTION = 'What number is missing in the progression?'


def generate_progression(first_num: int, step: int, length: int) -> list[int]:
    """Creates an arithmetic progression based on given parameters."""
    progression = []
    for i in range(length):
        progression.append(first_num + step * i)
    return progression


def generate_game() -> tuple[str, str]:
    """Release game logic and return parameters for game engine"""
    first_number = randint(MIN_NUMBER, MAX_NUMBER)
    step = randint(MIN_STEP, MAX_STEP)
    length = randint(MIN_LENGTH, MAX_LENGTH)
    hidden_index = randint(0, length - 1)
    progression = generate_progression(first_number, step, length)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = '..'
    question = ' '.join(map(str, progression))
    return question, correct_answer
