from brain_games.cli import randomint


INSTRUCTION = 'Answer "yes" if given number is prime. Otherwise answer "no"'


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def generate():
    random = randomint()
    if is_even(random) is True:
        return random, 'yes'
    else:
        return random, 'no'
