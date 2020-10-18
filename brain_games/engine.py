from brain_games.games.cli import welcome_user
import prompt


def greeting(game):
    result, question, uniqe_text = game()
    print('Welcome to the Brain Games!')
    print(uniqe_text)
    name, welcome = welcome_user()
    print('\n' + welcome)
    return name


def run(game):
    times_of_repeating = 3
    name = greeting(game)
    while times_of_repeating != 0:
        result, question, uniqe_text = game()
        print('Question: ' + question)
        answer = prompt.string('Your answer: ')
        if result == answer:
            print('Correct!')
            times_of_repeating -= 1
        else:
            answer_is_wrong = f'''"{answer}" is wrong answer ;(.
Correct answer was "{result}"
Let's try again, {name}!'''
            return print(answer_is_wrong)
    return(print('Congratulations, ' + name + '!'))
