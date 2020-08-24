from brain_games.games.calc import random_example_for_calc_game
from brain_games.games.even import random_number_for_even_game
from brain_games.games.gcd import random_num_for_gcd_game
from brain_games.games.prime import random_for_prime_game
from brain_games.games.progression import random_for_progression_game
from brain_games.games.cli import welcome_user


def greeting_for_calc_game():
    print('''Welcome to the Brain Games!
What is the result of the expression?
''')
    name, welcome = welcome_user()
    print('\n' + welcome)
    return name


def greeting_for_even_game():
    print('''Welcome to the Brain Games!
Answer "yes" if number even otherwise answer "no".
''')
    name, welcome = welcome_user()
    print('\n' + welcome)
    return name


def greeting_for_gcd_game():
    print('''Welcome to the Brain Games!
Find the greatest common divisor of given numbers.
''')
    name, welcome = welcome_user()
    print('\n' + welcome)
    return name


def greeting_for_prime_game():
    print('''Welcome to the Brain Games!
Answer "yes" if given number is prime. Otherwise answer "no".
''')
    name, welcome = welcome_user()
    print('\n' + welcome)
    return name


def greeting_for_progression_game():
    print('''Welcome to the Brain Games!
What number is missing in the progression?
''')
    name, welcome = welcome_user()
    print('\n' + welcome)
    return name


def run(game):
    if game == 'calc':
        random_example_for_calc_game(greeting_for_calc_game())
        return
    elif game == 'even':
        random_number_for_even_game(greeting_for_even_game())
        return
    elif game == 'gcd':
        random_num_for_gcd_game(greeting_for_gcd_game())
        return
    elif game == 'prime':
        random_for_prime_game(greeting_for_prime_game())
        return
    elif game == 'progression':
        random_for_progression_game(greeting_for_progression_game())
        return
    else:
        print('Такой игры нету :(')
        return
