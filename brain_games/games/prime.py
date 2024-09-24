from random import randint


MIN_NUMBER = 0
MAX_NUMBER = 10
DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num: int) -> str:
    FIRST_DIVIDER = 2
    middle_divider = int(num ** 0.5 + 1)
    if num < FIRST_DIVIDER:
        return 'no'
    for i in range(FIRST_DIVIDER, middle_divider):
        if num % i == 0:
            return 'no'
    return 'yes'


def get_parametres() -> tuple[str, str]:
    number = randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = is_prime(number)
    question = str(number)
    return question, correct_answer
