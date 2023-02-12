from random import randint
import math


def condition():
    condition = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    print(condition)


def task():
    arguments = {}
    counter = 0
    while counter < 3:
        value = randint(1, 100)
        task = value
        if value > 2 and value % 2 == 0:
            correct_answer = 'no'
            arguments[task] = correct_answer
            counter += 1
        elif value >= 1 and value <= 3:
            correct_answer = 'yes'
            arguments[task] = correct_answer
            counter += 1
        else:
            step = 2
            sqrt_value = math.sqrt(value)
            for i in range(3, (int(sqrt_value) + 2), step):
                if value % i == 0:
                    correct_answer = 'no'
                    arguments[task] = correct_answer
                    break
                else:
                    correct_answer = 'yes'
                    arguments[task] = correct_answer
            counter += 1
    return arguments
