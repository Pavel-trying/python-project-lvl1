from random import randint


# разделил строку на две, потому что линтер ругается на длину
part_1_of_descriprion = 'Answer "yes" if given number is prime. '
part_2_of_descriprion = 'Otherwise answer "no".'
DESCRIPTION = part_1_of_descriprion + part_2_of_descriprion


def get_question_and_answer():
    question = randint(1, 100)
    result = 'yes'if is_num_prime(question) else 'no'
    return result, str(question)


def is_num_prime(num):
    counter = 2
    while counter <= num / 2:
        if num % counter == 0:
            return False
        counter += 1
    return True
