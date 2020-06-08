from brain_games.cli import randomint


INSTRUCTION = 'Answer "yes" if given number is prime. Otherwise answer "no"'


def even_data(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def start_game():
    random = randomint()
    game_parts = {}
    game_parts['quest'] = random
    game_parts['true_answer'] = even_data(random)
    return game_parts
