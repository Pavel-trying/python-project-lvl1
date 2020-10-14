from brain_games.games.calc import random_example_for_calc_game
from brain_games.games.even import random_number_for_even_game
from brain_games.games.gcd import random_num_for_gcd_game
from brain_games.games.prime import random_for_prime_game
from brain_games.games.progression import random_for_progression_game
from brain_games.games.cli import welcome_user
import prompt


def greeting(game):
    if game == 'calc':
        result, question, uniqe_text = random_example_for_calc_game()
    elif game == 'even':
        result, question, uniqe_text = random_number_for_even_game()
    elif game == 'gcd':
        result, question, uniqe_text = random_num_for_gcd_game()
    elif game == 'prime':
        result, question, uniqe_text = random_for_prime_game()
    elif game == 'progression':
        result, question, uniqe_text = random_for_progression_game()
    print('Welcome to the Brain Games!')
    print(uniqe_text)
    name, welcome = welcome_user()
    print('\n' + welcome)
    return name

"""
def run_calc():
    times_of_repeating = 3
    name = greeting(game)
    while times_of_repeating != 0:
        result, question, uniqe_text = random_example_for_calc_game()
        print('Question: ' + question)
        answer = prompt.string('Your answer: ')
        if result == answer:
            print('Correct!')
            times_of_repeating -= 1
        else:
            answer_is_wrong = f'''"{answer}" is wrong answer ;(.
Correct answer was "{result}"
Let's try again, {name}!'''
            return print(answer_is_wrong)
    return(print('Congratulations, ' + name + '!'))

def run_even():
    times_of_repeating = 3
    name = greeting(game)
    while times_of_repeating != 0:
        result, question, uniqe_text = random_number_for_even_game()
        print('Question: ' + question)
        answer = prompt.string('Your answer: ')
        if result == answer:
            print('Correct!')
            times_of_repeating -= 1
        else:
            answer_is_wrong = f'''"{answer}" is wrong answer ;(.
Correct answer was "{result}"
Let's try again, {name}!'''
            return print(answer_is_wrong)
    return(print('Congratulations, ' + name + '!'))

def run_gcd():
    times_of_repeating = 3
    name = greeting(game)
    while times_of_repeating != 0:
        result, question, uniqe_text = random_num_for_gcd_game()
        print('Question: ' + question)
        answer = prompt.string('Your answer: ')
        if result == answer:
            print('Correct!')
            times_of_repeating -= 1
        else:
            answer_is_wrong = f'''"{answer}" is wrong answer ;(.
Correct answer was "{result}"
Let's try again, {name}!'''
            return print(answer_is_wrong)
    return(print('Congratulations, ' + name + '!'))

def run_prime():
    times_of_repeating = 3
    name = greeting(game)
    while times_of_repeating != 0:
        result, question, uniqe_text = random_for_prime_game()
        print('Question: ' + question)
        answer = prompt.string('Your answer: ')
        if result == answer:
            print('Correct!')
            times_of_repeating -= 1
        else:
            answer_is_wrong = f'''"{answer}" is wrong answer ;(.
Correct answer was "{result}"
Let's try again, {name}!'''
            return print(answer_is_wrong)
    return(print('Congratulations, ' + name + '!'))

def run_progression():
    times_of_repeating = 3
    name = greeting(game)
    while times_of_repeating != 0:
        result, question, uniqe_text = random_for_progression_game()
        print('Question: ' + question)
        answer = prompt.string('Your answer: ')
        if result == answer:
            print('Correct!')
            times_of_repeating -= 1
        else:
            answer_is_wrong = f'''"{answer}" is wrong answer ;(.
Correct answer was "{result}"
Let's try again, {name}!'''
            return print(answer_is_wrong)
    return(print('Congratulations, ' + name + '!'))
"""

def run(game):
    times_of_repeating = 3
    name = greeting(game)
    while times_of_repeating != 0:
        if game == 'calc':
            result, question, uniqe_text = random_example_for_calc_game()
        elif game == 'even':
            result, question, uniqe_text = random_number_for_even_game()
        elif game == 'gcd':
            result, question, uniqe_text = random_num_for_gcd_game()
        elif game == 'prime':
            result, question, uniqe_text = random_for_prime_game()
        elif game == 'progression':
            result, question, uniqe_text = random_for_progression_game()
        print('Question: ' + question)
        answer = prompt.string('Your answer: ')
        if result == answer:
            print('Correct!')
            times_of_repeating -= 1
        else:
            answer_is_wrong = f'''"{answer}" is wrong answer ;(.
Correct answer was "{result}"
Let's try again, {name}!'''
            return print(answer_is_wrong)
    return(print('Congratulations, ' + name + '!'))

def run_calc():
    run('calc')

def run_even():
    run('even')

def run_gcd():
    run('gcd')

def run_prime():
    run('prime')

def run_progression():
    run('progression')
