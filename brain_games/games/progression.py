from random import randint


def condition():
    condition = 'What number is missing in the progression?'
    print(condition)


def task():
    arguments = {}
    counter = 0
    correct_answer = ''
    while counter < 3:
        start = randint(1, 50)
        step = randint(1, 10)
        skip = randint(0, 9)
        task = str(start)
        quantity = 1
        while quantity < 10:
            if quantity != skip:
                task += ' ' + str(start + step)
                start += step
                quantity += 1
            else:
                task += ' ..'
                correct_answer = start + step
                start += step
                quantity += 1
        arguments[task] = str(correct_answer)
        counter += 1
    return arguments
