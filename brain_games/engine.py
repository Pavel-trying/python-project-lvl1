from brain_games.games.calc import random_example_for_calc_game
from brain_games.games.even import random_number_for_even_game
from brain_games.games.gcd import random_num_for_gcd_game
from brain_games.games.prime import random_for_prime_game
from brain_games.games.progression import random_for_progression_game
from brain_games.games.cli import welcome_user
import prompt




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
    times_of_repeating = 3
    if game == 'calc':
        name = greeting_for_calc_game()
        while times_of_repeating != 0:
            result, question = random_example_for_calc_game()
            print('Question: ' + question)
            answer = prompt.string('Your answer: ')
            if result == answer:
                print('Correct!')
                times_of_repeating -= 1
            else:
                answer_is_wrong = (answer + " is wrong answer ;(. ")
                correct_was = ("Correct answer was " + result + "\nLet's try again, " + name + '!')
                return print(answer_is_wrong + correct_was)
        return(print('Congratulations, ' + name + '!'))
    
    elif game == 'even':
        name = greeting_for_even_game()
        while times_of_repeating != 0:
            result, question = random_number_for_even_game()
            print('Question: ' + str(question))
            answer = prompt.string('Your answer: ')
            if answer == result:
                print('Correct!')
                times_of_repeating -= 1
            else:
                answer_is_wrong = (answer + " is wrong answer ;(. ")
                correct_was = ("Correct answer was " + result + "\nLet's try again, " + name + '!')
                return print(answer_is_wrong + correct_was)
        return(print('Congratulations, ' + name + '!'))

    elif game == 'gcd':
        name = greeting_for_gcd_game()
        while times_of_repeating != 0:
            result, question = random_num_for_gcd_game()
            print('Question: ' + question)
            answer = prompt.string('Your answer: ')
            if result == answer:
                print('Correct!')
                times_of_repeating -= 1
            else:
                answer_is_wrong = (answer + " is wrong answer ;(. ")
                correct_was = ("Correct answer was " + result + "\nLet's try again, " + name + '!')
                return print(answer_is_wrong + correct_was)
        return(print('Congratulations, ' + name + '!'))

    elif game == 'prime':
        name = greeting_for_prime_game()
        while times_of_repeating != 0:
            result, question = random_for_prime_game()
            print('Question: ' + question)
            answer = prompt.string('Your answer: ')
            if result == answer:
                print('Correct!')
                times_of_repeating -= 1
            else:
                answer_is_wrong = (answer + " is wrong answer ;(. ")
                correct_was = ("Correct answer was " + result + "\nLet's try again, " + name + '!')
                return print(answer_is_wrong + correct_was)
        return(print('Congratulations, ' + name + '!'))

    elif game == 'progression':
        name = greeting_for_progression_game()
        while times_of_repeating != 0:
            result, question = random_for_progression_game()
            print('Question: ' + question)
            answer = prompt.string('Your answer: ')
            if result == answer:
                print('Correct!')
                times_of_repeating -= 1
            else:
                answer_is_wrong = (answer + " is wrong answer ;(. ")
                correct_was = ("Correct answer was " + result + "\nLet's try again, " + name + '!')
                return print(answer_is_wrong + correct_was)
        return(print('Congratulations, ' + name + '!'))

    else:
        print('Такой игры нету :(')
        return

    