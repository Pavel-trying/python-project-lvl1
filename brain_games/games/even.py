from random import randint


def description():
    uniqe_text = 'Answer "yes" if number even otherwise answer "no".\n'
    return(uniqe_text)


def game_function():
    number = randint(1, 99)
    question = number
    if number % 2 != 0:
        result = 'no'
    elif number % 2 == 0:
        result = 'yes'
    return result, str(question)
