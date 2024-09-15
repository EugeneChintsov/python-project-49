from brain_games.cli import welcome_user
from brain_games.logic import quest


# Player = welcome_user()
# name_of_game = 'even'


def main(Player=welcome_user(), name_of_game='even'):
    # print('Answer "yes" if the number is even, otherwise answer "no".')
    quest(Player, name_of_game)


if __name__ == '__main__':
    main()
