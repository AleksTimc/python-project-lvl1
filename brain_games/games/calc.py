from operator import sub, mul, add
import random


INSTRUCTION = 'What is the result of the expression?'


OPERATIONS = (('-', sub), ('*', mul), ('+', add))


def generate_data():
    num_one = random.randint(1, 50)
    num_two = random.randint(1, 50)
    sign, operator = random.choice(OPERATIONS)
    question = str(num_one) + ' ' + sign + ' ' + str(num_two)
    true_answer = str(operator(num_one, num_two))
    return question, true_answer
