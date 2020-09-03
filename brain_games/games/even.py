def random_number_for_even_game():
    from random import randint
    number = randint(1, 99)
    question = number
    if number % 2 != 0:
        result = 'no'
    elif number % 2 == 0:
        result = 'yes'
    return result, str(question)
