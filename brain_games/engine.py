"""This module describes the general logic for all games."""
import prompt


QUESTION_COUNT = 3


def run(game):
    """Launches the game using the passed game parameters."""
    description = game.DESCRIPTION
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? \n')
    print(f'Hello, {username}!')
    print(description)
    for n in range(QUESTION_COUNT):
        question, correct_answer = game.get_parameters()
        print(f'Question: {question} ')
        answer = prompt.string('Your answer: ')
        if correct_answer == answer:
            print('Correct!')
        else:
            print(f'"{answer}" is wrong answer ;(. '
                  f'Correct answer was "{correct_answer}".\n'
                  f'Let\'s try again, {username}!')
            return
    print(f'Congratulations, {username}!')
