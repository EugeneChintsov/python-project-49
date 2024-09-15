from brain_games.cli import welcome_user
from brain_games.logic import quest


# Player = welcome_user()
# name_of_game = 'calc'


def main(Player=welcome_user(), name_of_game='calc'):
    # print('What is the result of the expression?')
    quest(Player, name_of_game)


if __name__ == '__main__':
    main()
