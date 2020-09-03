def random_num_for_gcd_game():
    from random import randint
    first_num = randint(1, 100)
    sec_num = randint(1, 100)
    question = str(first_num) + ' ' + str(sec_num)
    while first_num != 0 and sec_num != 0:
        if first_num > sec_num:
            first_num %= sec_num
        else:
            sec_num %= first_num
        result = first_num + sec_num
    return str(result), question
