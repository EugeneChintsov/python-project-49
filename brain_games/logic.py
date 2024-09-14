import random


def is_even(num):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'


def rand_number(begin=-10, end=10):
    return random.randint(begin, end)


def calc(operator, n1, n2):
    if operator == '+':
        result = n1 + n2
    elif operator == '-':
        result = n1 - n2
    elif operator == '*':
        result = n1 * n2
    elif operator == '/':
        result = n1 / n1 if n2 == 0 else n1 / n2
    return result


def even_quest(name, question_count=3):
    for n in range(question_count):
        # operator = random.choice(['+', '-', '*', '/'])
        n1 = rand_number()
        # n2 = rand_number()
        # =============================================
        correct_answer = is_even(n1)
        question = n1
        # =============================================
        print(f'Question: {question}')
        answer = input('Your answer: ')
        if correct_answer == answer.lower():
            print('Correct!')
        else:
            print(f'"{answer}" is wrong answer ;(. '
                  + f'Correct answer was "{correct_answer}".\n'
                  + f'Let\'s try again, {name}!')
            break
        if n == question_count - 1:
            print(f'Congratulations, {name}!')


def calc_quest(name, question_count=3):
    for n in range(question_count):
        operator = random.choice(['+', '-', '*', '/'])
        n1 = rand_number()
        n2 = rand_number()
        # =============================================
        correct_answer = str(calc(operator, n1, n2))
        question = f'{n1} {operator} {n2}'
        # =============================================
        print(f'Question: {question} ')
        answer = input('Your answer: ')
        print('correct answer: ' + str(type(correct_answer)))
        print('answer: ' + str(type(answer)))
        if correct_answer == answer:
            print('Correct!')
        else:
            print(f'"{answer}" is wrong answer ;(. '
                  + f'Correct answer was "{correct_answer}".\n'
                  + f'Let\'s try again, {name}!')
            break
        if n == question_count - 1:
            print(f'Congratulations, {name}!')
