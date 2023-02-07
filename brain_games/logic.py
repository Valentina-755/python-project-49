import prompt


def welcome():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name


def round(dictionary, name):
    for task, cor_answer in dictionary.items():
        print('Question: ' + str(task))
        user_answer = input('Your answer: ')
        if user_answer == cor_answer:
            print('Correct!')
        else:
            print(f'''"{user_answer}" is wrong answer ;(. Correct answer was "{cor_answer}".
Let's try again, {name}!''')
            return
    print('Congratulations, ' + name + '!')
