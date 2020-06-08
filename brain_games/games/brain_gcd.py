from brain_games.cli import randomint


INSTRUCTION = 'Find the greatest common divisor of given numbers.'


def gcd_data(number1, number2):
    while number1 != 0 and number2 != 0:
        if number1 > number2:
            number1 = number1 % number2
        else:
            number2 = number2 % number1
    return number1 + number2


def start_game():
    num_one = randomint()
    num_two = randomint()
    game_parts = {}
    game_parts['quest'] = str(num_one) + ' ' + str(num_two)
    game_parts['true_answer'] = gcd_data(num_one, num_two)
    return game_parts
