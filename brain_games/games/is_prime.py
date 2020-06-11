from brain_games.cli import randomint


INSTRUCTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    for digit in range(2, number):
        if (number % digit) == 0:
            return False
        elif (number // digit) == 1:
            return True


def generate():
    random = randomint()
    if is_prime(random):
        return random, 'yes'
    else:
        return random, 'no'
