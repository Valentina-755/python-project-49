from random import randint


def condition():
    condition = 'Answer "yes" if the number is even, otherwise answer "no".'
    print(condition)


def task():
    arguments = {}
    counter = 0
    while counter < 3:
        task = randint(1, 100)
        if task % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        arguments[task] = correct_answer
        counter += 1
    return arguments

