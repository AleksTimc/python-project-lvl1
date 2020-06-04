from brain_games.cli import randomint


def is_prime():
    random = randomint()
    game_parts = {}
    game_parts['instruction'] = 'Answer "yes" if given number' \
                                ' is prime. Otherwise answer "no".'
    game_parts['quest'] = random
    for digit in range(2, random):
        if (random % digit) == 0:
            game_parts['true_answer'] = 'no'
            break
        elif (random // digit) == 1:
            game_parts['true_answer'] = 'yes'
            break
    return game_parts


def main():
    is_prime()
