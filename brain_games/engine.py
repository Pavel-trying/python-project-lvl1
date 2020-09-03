from brain_games.games.calc import random_example_for_calc_game
from brain_games.games.even import random_number_for_even_game
from brain_games.games.gcd import random_num_for_gcd_game
from brain_games.games.prime import random_for_prime_game
from brain_games.games.progression import random_for_progression_game
from brain_games.games.cli import welcome_user
import prompt


def greeting(game):
    if game == 'calc':
        uniqe_text = 'What is the result of the expression?\n'
    elif game == 'even':
        uniqe_text = 'Answer "yes" if number even otherwise answer "no".\n'
    elif game == 'gcd':
        uniqe_text = 'Find the greatest common divisor of given numbers.\n'
    elif game == 'prime':
        # разделил строку на две, потому что линтер ругается на длину
        uniqe_text = 'Answer "yes" if given number is prime. '
        uniqe_text += 'Otherwise answer "no".\n'
    elif game == 'progression':
        uniqe_text = 'What number is missing in the progression?\n'
    print('Welcome to the Brain Games!')
    print(uniqe_text)
    name, welcome = welcome_user()
    print('\n' + welcome)
    return name


def run(game):
    times_of_repeating = 3
    name = greeting(game)
    while times_of_repeating != 0:
        if game == 'calc':
            result, question = random_example_for_calc_game()
        elif game == 'even':
            result, question = random_number_for_even_game()
        elif game == 'gcd':
            result, question = random_num_for_gcd_game()
        elif game == 'prime':
            result, question = random_for_prime_game()
        elif game == 'progression':
            result, question = random_for_progression_game()
        print('Question: ' + question)
        answer = prompt.string('Your answer: ')
        if result == answer:
            print('Correct!')
            times_of_repeating -= 1
        else:
            answer_is_wrong = (answer + " is wrong answer ;(. ")
            correct_was = ("Correct answer was " + result)
            try_again = "\nLet's try again, " + name + '!'
            return print(answer_is_wrong + correct_was + try_again)
    return(print('Congratulations, ' + name + '!'))
