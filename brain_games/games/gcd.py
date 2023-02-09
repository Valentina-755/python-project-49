from random import randint
import math


def condition():
    condition = 'Find the greatest common divisor of given numbers.'
    print(condition)


def task():
    arguments = {}
    counter = 0
    while counter < 3:
        elem_1 = randint(1, 20)
        elem_2 = randint(1, 20)
        task = str(elem_1) + ' ' + str(elem_2)
        correct_answer = math.gcd(elem_1, elem_2)
        arguments[task] = str(correct_answer)
        counter += 1
    return arguments
