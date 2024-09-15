#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.logic import quest


def main():
    Player = welcome_user()
    name_of_game = input('Choose game type (even/calc): ').lower()

    quest(Player, name_of_game)


if __name__ == '__main__':
    main()
