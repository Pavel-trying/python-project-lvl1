from brain_games.games.progression import greeting_for_progression_game
from brain_games.games.progression import random_for_progression_game


def main():
    name = greeting_for_progression_game()
    random_for_progression_game(name)


if __name__ == '__main__':
    main()
