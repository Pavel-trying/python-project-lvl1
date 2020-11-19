from random import randint, choice


DESCRIPTION = 'What is the result of the expression?'


def get_question_and_answer():
    choise_sign = choice('-+*')
    first_num = randint(25, 50)
    sec_num = randint(1, 25)
    if choise_sign == ('+'):
        result = first_num + sec_num
    elif choise_sign == ('-'):
        result = first_num - sec_num
    else:
        result = first_num * sec_num
    question = f"{str(first_num)} {choise_sign} {str(sec_num)}"
    return str(result), question
