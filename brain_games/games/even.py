import random


INSTRUCTION = 'Answer "yes" if number even otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def generate_data():
    game_question = random.randint(1, 50)
    true_answer = 'no'
    if is_even(game_question):
        true_answer = 'yes'
    return game_question, true_answer
