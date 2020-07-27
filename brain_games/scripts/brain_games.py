import sys
sys.path.append("/home/pavel/python-project-lvl1/brain_games/games")
from cli import welcome_user # noqa


def main():
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
