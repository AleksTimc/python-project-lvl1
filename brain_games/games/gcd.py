import random


INSTRUCTION = 'Find the greatest common divisor of given numbers.'


def gcd(number1, number2):
    while number1 != 0 and number2 != 0:
        if number1 > number2:
            number1 = number1 % number2
        else:
            number2 = number2 % number1
    return number1 + number2


def generate_data():
    num_one = random.randint(1, 50)
    num_two = random.randint(1, 50)
    question = str(num_one) + ' ' + str(num_two)
    true_answer = str(gcd(num_one, num_two))
    return question, true_answer
