import prompt
import random


def welcome_user():
    print()
    name = prompt.string('May I have your name? ')
    print("Hello, {}!". format(name))
    return name


def answer():
    answer = prompt.string('Your answer: ')
    return answer


def randomint():
    randomint = random.randint(1, 50)
    return randomint


def randstep():
    randstep = random.randint(1, 10)
    return randstep


def randstep_quest():
    randstep_quest = random.randint(0, 9)
    return randstep_quest


def rand_operator():
    operatorlist = ['*', '+', '-']
    return random.choice(operatorlist)


def greet():
    print('Welcome to the Brain Games!')


def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False
