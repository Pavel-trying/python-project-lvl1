def random_for_progression_game():
    from random import randint
    start_num = randint(1, 100)
    position_of_indefinite_num = randint(1, 9)
    value_of_progression = randint(1, 30)
    index_of_repeats = 1
    if position_of_indefinite_num == 1:
        question = ('..')
        result = start_num
        index_of_repeats += 1
    else:
        question = str(start_num)
    while index_of_repeats <= 10:
        if position_of_indefinite_num == index_of_repeats:
            question += (' ..')
            start_num += value_of_progression
            index_of_repeats += 2
            result = start_num
        else:
            start_num += value_of_progression
            question += (' ' + str(start_num))
            index_of_repeats += 1
    return str(result), question
