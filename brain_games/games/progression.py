from random import randint


DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_answer():
    quantity_of_nums_in_question = 10
    start_num = randint(1, 100)
    position_of_indefinite_num = randint(1, quantity_of_nums_in_question - 1)
    value_of_progression = randint(1, 30)
    index_of_repeats = 1
    if position_of_indefinite_num == 1:
        question = ('..')
        result = start_num
        index_of_repeats += 1
    else:
        question = str(start_num)
    while index_of_repeats <= quantity_of_nums_in_question:
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
