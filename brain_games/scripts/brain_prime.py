import sys
sys.path.append("/home/pavel/python-project-lvl1/brain_games/games")
from prime import greeting_prime, random_prime # noqa


def main():
    name = greeting_prime()
    random_prime(name)


if __name__ == '__main__':
    main()
