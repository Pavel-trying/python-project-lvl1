def random_example_for_calc_game():
    from random import randint, choice
    choise_sign = choice('-+*')
    first_num = randint(0, 100)
    sec_num = randint(1, 100)
    firstNumMult = randint(1, 50)
    secNumMult = randint(1, 20)
    if choise_sign == ('+'):
        result = first_num + sec_num
        question = str(first_num) + ' + ' + str(sec_num)
    elif choise_sign == ('-'):
        if first_num <= sec_num:
            result = sec_num - first_num
            question = str(sec_num) + ' - ' + str(first_num)
        else:
            result = first_num - sec_num
            question = str(first_num) + ' - ' + str(sec_num)
    else:
        result = firstNumMult * secNumMult
        question = str(firstNumMult) + ' * ' + str(secNumMult)

    return str(result), question
