def random_for_prime_game():
    from random import randint
    question = randint(1, 100)
    index = question
    for n in range(index + 1):
        for x in range(2, n):
            if n % x == 0 and n == question:
                result = "no"
                break
        else:
            result = 'yes'
    return result, str(question)
