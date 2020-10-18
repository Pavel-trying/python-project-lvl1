from random import randint


def random_for_prime_game():
    # разделил строку на две, потому что линтер ругается на длину
    uniqe_text = 'Answer "yes" if given number is prime. '
    uniqe_text += 'Otherwise answer "no".\n'
    question = randint(1, 100)
    index = question
    for n in range(index + 1):
        for x in range(2, n):
            if n % x == 0 and n == question:
                result = "no"
                break
        else:
            result = 'yes'
    return result, str(question), uniqe_text
