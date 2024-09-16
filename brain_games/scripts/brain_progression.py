from brain_games.cli import welcome_user
from brain_games.logic import quest


def main(Player=welcome_user(), name_of_game='progression'):

    quest(Player, name_of_game)


if __name__ == '__main__':
    main()
