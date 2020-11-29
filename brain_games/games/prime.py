from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime.' \
                ' Otherwise answer "no".'


def get_question_and_answer():
    question = randint(1, 100)
    result = 'yes'if is_prime(question) else 'no'
    return result, str(question)


def is_prime(num):
    if num <= 1:
        return False
    else:
        counter = 2
        while counter <= num / 2:
            if num % counter == 0:
                return False
            counter += 1
        return True
