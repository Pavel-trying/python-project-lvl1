import sys
sys.path.append("/home/pavel/python-project-lvl1/brain_games/games")
from gcd import greeting_gcd, random_num_gcd # noqa


def main():
    name = greeting_gcd()
    random_num_gcd(name)


if __name__ == '__main__':
    main()
