import sys
sys.path.append("/home/pavel/python-project-lvl1/brain_games/games")
from even import greeting, random_number # noqa


def main():
    name = greeting()
    random_number(name)


if __name__ == '__main__':
    main()
