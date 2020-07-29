from brain_games.games.prime import greeting_for_prime_game
from brain_games.games.prime import random_for_prime_game


def main():
    name = greeting_for_prime_game()
    random_for_prime_game(name)


if __name__ == '__main__':
    main()
