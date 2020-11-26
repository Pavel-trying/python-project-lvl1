from random import randint


DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_answer():
    quantity_of_nums_in_question = 10
    start_num = randint(1, 100)
    position_of_indefinite_num = randint(0, quantity_of_nums_in_question - 1)
    value_of_progression = randint(1, 30)
    index_of_num = 0
    question = ''
    while index_of_num < quantity_of_nums_in_question:
        if index_of_num == position_of_indefinite_num:
            question += '. . '
            index_of_num += 1
        else:
            question += f'{start_num + value_of_progression * index_of_num} '
            index_of_num += 1
    result = start_num + value_of_progression * position_of_indefinite_num
    return str(result), question.rstrip()
