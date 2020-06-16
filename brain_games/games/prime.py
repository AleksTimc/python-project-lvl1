import random

INSTRUCTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    for digit in range(2, number):
        if (number % digit) == 0:
            return False
        elif (number // digit) == 1:
            return True
    return False


def generate_data():
    random_number = random.randint(1, 50)
    if is_prime(random_number):
        true_answer = 'yes'
        return random_number, true_answer
    true_answer = 'no'
    return random_number, true_answer
