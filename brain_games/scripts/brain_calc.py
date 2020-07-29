from brain_games.games.calc import greeting_for_calc_game
from brain_games.games.calc import random_example_for_calc_game


def main():
    name = greeting_for_calc_game()
    random_example_for_calc_game(name)


if __name__ == '__main__':
    main()
