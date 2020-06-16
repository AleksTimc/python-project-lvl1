from operator import sub, mul, add
import random


INSTRUCTION = 'What is the result of the expression?'


OPERATORS = (('-', sub), ('*', mul), ('+', add))


def generate_data():
    num_one = random.randint(1, 50)
    num_two = random.randint(1, 50)
    sign, operator = random.choice(OPERATORS)
    question = str(num_one) + ' ' + sign + ' ' + str(num_two)
    true_answer = operator(num_one, num_two)
    return question, true_answer
