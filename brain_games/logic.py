import random


def is_even(num):
    if num % 2 == 0:
        return 'Yes'
    else:
        return 'No'

def even_quest(name, question_count=3):
    for n in range(question_count):
        question = random.randint(1, 100)
        print(f'Question: {question}')
        answer = input('Your answer: ')
        if is_even(question).lower() == answer.lower():
            print('Correct!')
        else:
            print(f'"{answer}" is wrong answer ;(. '
                  + f'Correct answer was "{is_even(question)}".\n'
                  + f'Let\'s try again, {name}!')
            break
        if n == question_count - 1:
            print(f'Congratulations, {name}!')
