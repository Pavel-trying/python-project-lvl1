from brain_games.games.gcd import greeting_for_gcd_game
from brain_games.games.gcd import random_num_for_gcd_game


def main():
    name = greeting_for_gcd_game()
    random_num_for_gcd_game(name)


if __name__ == '__main__':
    main()
