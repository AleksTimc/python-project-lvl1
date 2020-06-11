from brain_games.cli import randomint
from operator import sub, mul, add
import random


INSTRUCTION = 'What is the result of the expression?'


OPERATORS = (('-', sub), ('*', mul), ('+', add))


def generate():
    num_one = randomint()
    num_two = randomint()
    sign, oper = random.choice(OPERATORS)
    question = str(num_one) + ' ' + sign + ' ' + str(num_two)
    true_answer = oper(num_one, num_two)
    return question, true_answer
