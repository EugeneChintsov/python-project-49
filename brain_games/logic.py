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
    return int(result)


def gcd(n1, n2):
    if n2 == 0:
        return n1
    else:
        return gcd(n2, n1 % n2)


def quest(name, name_of_game, question_count=3):
    for n in range(question_count):
        match name_of_game:
            case 'calc':
                Intro = 'What is the result of the expression?'
                operator = random.choice(['+', '-', '*', '/'])
                n1 = rand_number()
                n2 = rand_number()
                correct_answer = str(calc(operator, n1, n2))
                question = f'{n1} {operator} {n2}'
            case 'even':
                Intro = 'Answer "yes" if the number is even, otherwise answer "no".'
                n1 = rand_number()
                correct_answer = is_even(n1)
                question = n1
            case 'gcd':
                Intro = 'Find the greatest common divisor of given numbers.'
                n1 = rand_number()
                n2 = rand_number()
                correct_answer = str(abs(gcd(n1, n2)))
                question = f'{n1} and {n2}'
            case _:
                print('GoodBye!')
                break

        print(Intro)
        print(f'Question: {question} ')
        answer = input('Your answer: ')
        if correct_answer == answer:
            print('Correct!')
        else:
            print(f'"{answer}" is wrong answer ;(. '
                  + f'Correct answer was "{correct_answer}".\n'
                  + f'Let\'s try again, {name}!')
            break
        if n == question_count - 1:
            print(f'Congratulations, {name}!')
