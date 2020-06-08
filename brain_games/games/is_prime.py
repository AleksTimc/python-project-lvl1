from brain_games.cli import randomint


INSTRUCTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    for digit in range(2, number):
        if (number % digit) == 0:
            return 'no'
        elif (number // digit) == 1:
            return 'yes'


def start_game():
    random = randomint()
    game_parts = {}
    game_parts['quest'] = random
    game_parts['true_answer'] = is_prime(random)
    return game_parts
