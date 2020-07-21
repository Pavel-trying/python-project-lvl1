def welcome_user():
    import prompt
    name = prompt.string('May I have your name? ')
    template = "{}, {}!"
    print(template.format('Hello', name))