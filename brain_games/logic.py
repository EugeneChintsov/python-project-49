import random


def is_even(num):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'


def rand_number(begin=-10, end=10) -> int:
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


def arifmetical_prog(first_num, diff_num, len_prog):
    prog = []
    for i in range(len_prog):
        prog.append(first_num + diff_num * i)
    return prog


def is_prime(num):
    if num < 2:
        return 'no'
    for i in range(2, int(num ** 0.5 + 1)):
        if num % i == 0:
            return 'no'
    return 'yes'


def quest(name, name_of_game, question_count=3):
    for n in range(question_count):
        match name_of_game:
            case 'even':
                Intro = 'Answer "yes" if the number is even, otherwise answer "no".'
                n1 = rand_number()
                correct_answer = is_even(n1)
                question = str(n1)
            case 'calc':
                Intro = 'What is the result of the expression?'
                operator = random.choice(['+', '-', '*', '/'])
                n1 = rand_number()
                n2 = rand_number()
                correct_answer = str(calc(operator, n1, n2))
                question = f'{n1} {operator} {n2}'
            case 'gcd':
                Intro = 'Find the greatest common divisor of given numbers.'
                n1 = rand_number()
                n2 = rand_number()
                correct_answer = str(abs(gcd(n1, n2)))
                question = f'{n1} and {n2}'
            case 'progression':
                Intro = 'What number is missing in the progression?'
                n1 = rand_number()
                n2 = rand_number(1, 10)
                n3 = rand_number(5, 10)
                n4 = rand_number(0, n3 - 1)
                prog = arifmetical_prog(n1, n2, n3)
                correct_answer = str(prog[n4])
                prog[n4] = '..'
                question = ' '.join(map(str, prog))
            case 'prime':
                Intro = 'Answer "yes" if given number is prime. Otherwise answer "no".'
                n1 = rand_number()
                correct_answer = is_prime(n1)
                question = str(n1)
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
