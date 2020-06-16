import random


INSTRUCTION = 'Answer "yes" if number even otherwise answer "no".'


def is_even(number):
    if number % 2 == 0:
        return True


def generate_data():
    random_number = random.randint(1, 50)
    if is_even(random_number):
        true_answer = 'yes'
        return random_number, true_answer
    true_answer = 'no'
    return random_number, true_answer
