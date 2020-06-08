from brain_games.cli import randomint
import random


INSTRUCTION = 'What is the result of the expression?'


def rand_operator():
    operatorlist = ['*', '+', '-']
    return random.choice(operatorlist)


def calc_data(number1, operator, number2):
    if operator == '*':
        return number1 * number2
    elif operator == '-':
        return number1 - number2
    else:
        return number1 + number2


def start_game():
    num_one = randomint()
    num_two = randomint()
    oper = rand_operator()
    game_parts = {}
    game_parts['quest'] = str(num_one) + ' ' + oper + ' ' + str(num_two)
    game_parts['true_answer'] = calc_data(num_one, oper, num_two)
    return game_parts
