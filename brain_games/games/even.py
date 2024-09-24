from random import randint


MIN_NUMBER = -10
MAX_NUMBER = 10
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num: int) -> str:
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'


def get_parametres() -> tuple[str, str]:
    number = randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = is_even(number)
    question = str(number)
    return question, correct_answer
