from brain_games.games.cli import welcome_user
import prompt


def run(game):
    times_of_repeating = 3
    print('Welcome to the Brain Games!')
    print(game.description())
    name, welcome = welcome_user()
    print('\n' + welcome)
    while times_of_repeating != 0:
        result, question, = game.game_function()
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
