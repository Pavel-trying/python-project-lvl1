def greeting_for_even_game():
    from brain_games.games.cli import welcome_user
    print('''Welcome to the Brain Games!
Answer "yes" if number even otherwise answer "no".
''')
    name, welcome = welcome_user()
    print('\n' + welcome)
    return name


def random_number_for_even_game(name):
    from random import randint
    import prompt
    numbs_of_correct_answers = 0
    # разделил две строки на четыреы, потому что линтер ругается на их длину
    yes_wrong = ("'yes' is wrong answer ;(. ")
    correct_no = ("Correct answer was 'no'\nLet's try again, " + name + '!')
    no_wrong = ("'no' is wrong answer ;(. ")
    correct_yes = ("Correct answer was 'yes'\nLet's try again, " + name + '!')
    while numbs_of_correct_answers != 3:
        number = randint(1, 99)
        print('Question: ' + str(number))
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
            # решил немного доработать, чтобы заново не стартовать
            # игру каждый раз при ошибке
            print("Please, type just 'yes' or 'no'!")
    return(print('Congratulations, ' + name + '!'))
