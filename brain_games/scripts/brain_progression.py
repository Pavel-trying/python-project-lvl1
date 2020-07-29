from brain_games.games.progression import greeting_progression
from brain_games.games.progression import random_progression


def main():
    name = greeting_progression()
    random_progression(name)


if __name__ == '__main__':
    main()
