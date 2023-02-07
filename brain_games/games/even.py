from random import randint


def condition():
    condition = 'Answer "yes" if the number is even, otherwise answer "no".'
    print(condition)


def task():
    task = randint(1, 100)
    return task


def correct_answer(t):
    if t % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer


