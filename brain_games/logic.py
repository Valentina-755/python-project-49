import prompt


def welcome():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name


def round(dictionary, name):
    for task, c_an in dictionary.items():
        print('Question: ' + str(task))
        u_an = input('Your answer: ')
        if u_an == c_an:
            print('Correct!')
        else:
            print(f'''"{u_an}" is wrong answer ;(. Correct answer was "{c_an}".
Let's try again, {name}!''')
            return
    print('Congratulations, ' + name + '!')
