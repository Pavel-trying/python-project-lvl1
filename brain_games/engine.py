import prompt


def run(game):
    number_of_questions = 3
    print('Welcome to the Brain Games!')
    print(game.DESCRIPTION + '\n')
    name = prompt.string('May I have your name? ')
    welcome = f'Hello, {name}'
    print('\n' + welcome)
    while number_of_questions != 0:
        result, question, = game.get_question_and_answer()
        print('Question: ' + question)
        answer = prompt.string('Your answer: ')
        if result == answer:
            print('Correct!')
            number_of_questions -= 1
        else:
            answer_is_wrong = f'''"{answer}" is wrong answer ;(. Correct answer was "{result}"
Let's try again, {name}!'''
            return print(answer_is_wrong)
    print('Congratulations, ' + name + '!')
