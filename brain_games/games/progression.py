def greeting_progression():
    from cli import welcome_user
    print('''Welcome to the Brain Games!
What number is missing in the progression?
''')
    name, welcome = welcome_user()
    print('\n' + welcome)
    return name


def random_progression(name):
    from random import randint
    import prompt
    numbs_of_correct_answers = 0
    while numbs_of_correct_answers != 3:
        start_num = randint(1, 100)
        undefinite_num_position = randint(1, 9)
        value_of_progression = randint(1, 30)
        index_of_repeats = 1
        if undefinite_num_position == 1:
            example = ('..')
            result = start_num
            index_of_repeats += 1
        else:
            example = str(start_num)
        while index_of_repeats <= 10:
            if undefinite_num_position == index_of_repeats:
                example += (' ..')
                start_num += value_of_progression
                index_of_repeats += 2
                result = start_num
            else:
                start_num += value_of_progression
                example += (' ' + str(start_num))
                index_of_repeats += 1
        print(example)
        answer = prompt.string('Your answer: ')
        if str(result) == str(answer):
            print('Correct!')
            numbs_of_correct_answers += 1
        else:
            wrong = ('"' + str(answer) + '"' + ' is wrong answer ')
            corr = (';(. Correct answer was ' + '"' + str(result) + '"' + '.')
            try_again = ("\nLet's try again, " + name + '!')
            return print(wrong + corr, try_again)
    return(print('Congratulations, ' + name + '!'))
