from random import randint


DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def get_question_and_answer():
    question = randint(1, 99)
    result = 'yes'if is_even(question) else 'no'
    return result, str(question)


def is_even(num):
    return num % 2 == 0
