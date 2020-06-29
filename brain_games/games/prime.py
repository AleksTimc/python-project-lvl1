import random

INSTRUCTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False
    for digit in range(2, int(number / 2)):
        if (number % digit) == 0:
            return False
        elif (number // digit) == 1:
            return True


def generate_data():
    random_number = random.randint(1, 50)
    true_answer = 'no'
    if is_prime(random_number):
        true_answer = 'yes'
    return random_number, true_answer
