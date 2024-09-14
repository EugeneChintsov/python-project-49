from brain_games.cli import welcome_user
from brain_games.logic import even_quest

Player = welcome_user()


def main():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    even_quest(Player)


if __name__ == '__main__':
    main()
