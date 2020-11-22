from random import randint, choice


DESCRIPTION = 'What is the result of the expression?'


def get_question_and_answer():
    sign = choice('-+*')
    first_num = randint(25, 50)
    sec_num = randint(1, 25)
    if sign == ('+'):
        result = first_num + sec_num
    elif sign == ('-'):
        result = first_num - sec_num
    elif sign == ('*'):
        result = first_num * sec_num
    question = f"{str(first_num)} {sign} {str(sec_num)}"
    return str(result), question
