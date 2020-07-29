def greeting_calc():
    from brain_games.games.cli import welcome_user
    print('''Welcome to the Brain Games!
What is the result of the expression?
''')
    name, welcome = welcome_user()
    print('\n' + welcome)
    return name


def random_example(name):
    from random import randint, choice
    import prompt
    numbs_of_correct_answers = 0
    while numbs_of_correct_answers != 3:
        choise_sign = choice('-+*')
        first_num = randint(0, 100)
        sec_num = randint(1, 100)
        firstNumMult = randint(1, 50)
        secNumMult = randint(1, 20)
        if choise_sign == ('+'):
            result = first_num + sec_num
            print('Question: ' + str(first_num) + ' + ' + str(sec_num))
        elif choise_sign == ('-'):
            if first_num <= sec_num:
                result = sec_num - first_num
                print('Question: ' + str(sec_num) + ' - ' + str(first_num))
            else:
                result = first_num - sec_num
                print('Question: ' + str(first_num) + ' - ' + str(sec_num))
        else:
            result = firstNumMult * secNumMult
            print('Question: ' + str(firstNumMult) + ' * ' + str(secNumMult))
        answer = prompt.string('Your answer: ')
        wrong_txt = ('"' + str(answer) + '"' + ' is wrong answer ')
        corr_txt = (';(. Correct answer was ' + '"' + str(result) + '"' + '.')
        try_again = ("\nLet's try again, " + name + '!')
        if str(result) == str(answer):
            print('Correct!')
            numbs_of_correct_answers += 1
        else:
            return print(wrong_txt + corr_txt, try_again)
    return(print('Congratulations, ' + name + '!'))
