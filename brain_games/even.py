def greeting():
    import sys
    sys.path.append("/home/pavel/python-project-lvl1/brain_games")
    from cli import welcome_user # noqa
    print('''Welcome to the Brain Games!
Answer "yes" if number even otherwise answer "no".
''')
    name, welcome = welcome_user()
    print(welcome)
    return name, welcome


def random_number(name):
    from random import randint
    import prompt
    numbs_of_correct_answers = 0
    yes_wrong = ("'yes' is wrong answer ;(. ")
    correct_no = ("Correct answer was 'no'\nLet's try again, " + name + '!')
    no_wrong = ("'no' is wrong answer ;(. ")
    correct_yes = ("Correct answer was 'yes'\nLet's try again, " + name + '!')
    while numbs_of_correct_answers != 3:
        number = randint(0, 99)
        print('\nQuestion: ' + str(number))
        answer = prompt.string('Your answer: ')
        if number % 2 != 0 and answer == 'yes':
            return print(yes_wrong + correct_no)
        elif number % 2 == 0 and answer == 'no':
            return print(no_wrong + correct_yes)
        elif number % 2 != 0 and answer == 'no':
            numbs_of_correct_answers += 1
            print('Correct!')
        elif number % 2 == 0 and answer == 'yes':
            numbs_of_correct_answers += 1
            print('Correct!')
        else:
            print("Please, type just 'yes' or 'no'!")
    return(print('Congratulations, ' + name + '!'))
