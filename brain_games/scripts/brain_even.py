import prompt
from random import randint


def greet():
    print('Welcome to the Brain Games!')


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name


def even():
    name = welcome_user()
    condition = 'Answer "yes" if the number is even, otherwise answer "no".'
    counter = 0
    print(condition)
    while counter < 3:
        randome_number = randint(1, 100)
        print('Question: ' + str(randome_number))
        user_answer = input('Your answer: ')
        if randome_number % 2 == 0:
            correct_answer = 'yes'
            incorrect_answer = 'no'
        else:
            correct_answer = 'no'
            incorrect_answer = 'yes'
        if user_answer == correct_answer:
            print('Correct!')
            counter +=1
        else:
            print(f'''"{user_answer}" is wrong answer ;(. Correct answer was "{correct_answer}".
Let's try again, {name}!''')
            return 
    print('Congratulations, ' + name + '!')



def main():
    greet()
    even()


if __name__ == '__main__':
    main()