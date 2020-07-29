def greeting_gcd():
    from brain_games.games.cli import welcome_user
    print('''Welcome to the Brain Games!
Find the greatest common divisor of given numbers.
''')
    name, welcome = welcome_user()
    print('\n' + welcome)
    return name


def random_num_gcd(name):
    from random import randint
    import prompt
    numbs_of_correct_answers = 0
    while numbs_of_correct_answers != 3:
        first_num = randint(1, 100)
        sec_num = randint(1, 100)
        print('Question: ' + str(first_num) + ' ' + str(sec_num))
        while first_num != 0 and sec_num != 0:
            if first_num > sec_num:
                first_num %= sec_num
            else:
                sec_num %= first_num
        result = first_num + sec_num
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
