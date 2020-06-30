import random

INSTRUCTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number > 2 and number <= 5:
        for digit in range(2, number):
            if number % digit == 0:
                return False
            return True
    if number > 5:
        for digit in range(2, round(number / 2)):
            if number % digit == 0:
                return False
            return True


def generate_data():
    question = random.randint(1, 50)
    true_answer = 'no'
    if is_prime(question):
        true_answer = 'yes'
    return question, true_answer
