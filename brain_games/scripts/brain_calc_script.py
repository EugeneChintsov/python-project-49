from brain_games.cli import welcome_user
from brain_games.logic import calc_quest

Player = welcome_user()


def main():
    print('What is the result of the expression?')
    calc_quest(Player)


if __name__ == '__main__':
    main()
