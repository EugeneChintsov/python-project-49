"""This module describes the general logic for all games."""
import prompt


QUESTION_COUNT = 3


def run(game: any) -> None:
    """Launches the game."""
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? \n')
    print(
        f'Hello, {username}!\n'
        f'{game.DESCRIPTION}'
    )
    for _ in range(QUESTION_COUNT):
        question, correct_answer = game.generate_game()
        print(f'Question: {question} ')
        answer = prompt.string('Your answer: ')
        if answer != correct_answer:
            print(
                f'"{answer}" is wrong answer ;(.'
                f'Correct answer was "{correct_answer}".\n'
                f'Let\'s try again, {username}!'
            )
            return
        print('Correct!')
    print(f'Congratulations, {username}!')
