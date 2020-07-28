def greeting_prime():
    from cli import welcome_user
    print('''Welcome to the Brain Games!
Answer "yes" if given number is prime. Otherwise answer "no".
''')
    name, welcome = welcome_user()
    print('\n' + welcome)
    return name


def random_prime(name):
    from random import randint
    import prompt
    numbs_of_correct_answers = 0
    while numbs_of_correct_answers != 3:
        num = randint(1, 100)
        index = num
        print(num)
        for n in range(index + 1):
            for x in range(2, n):
                if n % x == 0 and n == num:
                    result = ("no")
                    break
            else:
                result = ('yes')
        answer = prompt.string('Your answer: ')
        if result == answer:
            print('Correct!')
            numbs_of_correct_answers += 1
        else:
            wrong = ('"' + str(answer) + '"' + ' is wrong answer ')
            corr = (';(. Correct answer was ' + '"' + str(result) + '"' + '.')
            try_again = ("\nLet's try again, " + name + '!')
            return print(wrong + corr, try_again)
    return(print('Congratulations, ' + name + '!'))
