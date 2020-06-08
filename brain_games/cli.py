import prompt
import random


def welcome_user():
    print()
    name = prompt.string('May I have your name? ')
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


def game_engine2(game):
    greet()
    print(game.INSTRUCTION)
    name = welcome_user()
    print("Hello, {}!". format(name))
    rounds = 3
    attempt = 0
    while attempt < rounds:
        result = game.start_game()
        print('Question: ' + str(result['quest']))
        quest_answer = answer()
        if str(quest_answer) == str(result['true_answer']):
            print('Correct!')
            attempt += 1
        else:
            print(str(quest_answer) + " is wrong answer ;(."
                  "Correct answer was " + str(result['true_answer']) + ".")
            print("Let's try again," + name)
            break
    if attempt == rounds:
        print('Congratulations, ' + name)
