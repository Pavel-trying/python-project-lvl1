import sys
sys.path.append("/home/pavel/python-project-lvl1/brain_games/games")
from calc import greeting_calc, random_example # noqa


def main():
    name = greeting_calc()
    random_example(name)


if __name__ == '__main__':
    main()
