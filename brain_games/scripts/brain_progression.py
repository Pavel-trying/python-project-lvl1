import sys
sys.path.append("/home/pavel/python-project-lvl1/brain_games/games")
from progression import greeting_progression, random_progression # noqa


def main():
    name = greeting_progression()
    random_progression(name)


if __name__ == '__main__':
    main()
