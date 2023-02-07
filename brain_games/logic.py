import prompt


def logic():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    counter = 0
    condition()
    while counter < 3:
        t = task()
        cor_answer = correct_answer(t)
        print('Question: ' + str(t))
        user_answer = input('Your answer: ')
        if user_answer == cor_answer:
            print('Correct!')
            counter += 1
        else:
            print(f'''"{user_answer}" is wrong answer ;(. Correct answer was "{cor_answer}".
Let's try again, {name}!''')
            return
    print('Congratulations, ' + name + '!')
