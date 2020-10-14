from random import randint


def random_number_for_even_game():
    uniqe_text = 'Answer "yes" if number even otherwise answer "no".\n'
    number = randint(1, 99)
    question = number
    if number % 2 != 0:
        result = 'no'
    elif number % 2 == 0:
        result = 'yes'
    return result, str(question), uniqe_text
