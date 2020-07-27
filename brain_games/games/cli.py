def welcome_user():
    import prompt
    name = prompt.string('May I have your name? ')
    template = "{}, {}!"
    return name, template.format('Hello', name)
