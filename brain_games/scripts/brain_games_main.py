#!/usr/bin/env python3
from brain_games.cli import welcome_user
# from brain_games.scripts.brain_even import main as even_main
# from brain_games.scripts.brain_calc import main as calc_main
from brain_games.logic import quest


def main():
    Player = welcome_user()
    name_of_game = input('Choose game type (even/calc): ').lower()

    quest(Player, name_of_game)
    # if name_of_game.lower() == 'even':
    #    even_main(Player, 'even')
    # elif name_of_game.lower() == 'calc':
    #    calc_main(Player, 'calc')


if __name__ == '__main__':
    main()
