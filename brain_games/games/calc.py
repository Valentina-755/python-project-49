from random import randint, choice


def condition():
    condition = 'What is the result of the expression?.'
    print(condition)


def task():
    arguments = {}
    counter = 0
    while counter < 3:
        elem_1 = randint(1, 20)
        elem_2 = randint(1, 20)
        list = ['+', '-', '*']
        arithmetic = choice(list)
        if arithmetic == '+':
            task = str(elem_1) + ' ' + arithmetic + ' ' + str(elem_2)
            correct_answer = elem_1 + elem_2
        elif arithmetic == '-':
            task = str(elem_1) + ' ' + arithmetic + ' ' + str(elem_2)
            correct_answer = elem_1 - elem_2
        else:
            task = str(elem_1) + ' ' + arithmetic + ' ' + str(elem_2)
            correct_answer = elem_1 * elem_2
        arguments[task] = str(correct_answer)
        counter += 1
    return arguments
