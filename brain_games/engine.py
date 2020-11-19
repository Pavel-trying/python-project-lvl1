from brain_games.games.cli import welcome_user
import prompt


def run(game):
    times_of_repeating = 3
    print('Welcome to the Brain Games!')
    print(game.DESCRIPTION + '\n')
    name, welcome = welcome_user()
    print('\n' + welcome)
    while times_of_repeating != 0:
        result, question, = game.get_question_and_answer()
        print('Question: ' + question)
        answer = prompt.string('Your answer: ')
        if result == answer:
            print('Correct!')
            times_of_repeating -= 1
        else:
            answer_is_wrong = f'"{answer}" is wrong answer ;(. '
            correct_was = f'Correct answer was "{result}"'
            try_again = f"\nLet's try again, {name}!"
            return print(answer_is_wrong+correct_was+try_again)
    return(print('Congratulations, ' + name + '!'))
