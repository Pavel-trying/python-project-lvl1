from brain_games.games.even import greeting_for_even_game
from brain_games.games.even import random_number_for_even_game


def main():
    name = greeting_for_even_game()
    random_number_for_even_game(name)


if __name__ == '__main__':
    main()
