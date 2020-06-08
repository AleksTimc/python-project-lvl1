from brain_games.cli import randomint


INSTRUCTION = 'Answer "yes" if given number is prime. Otherwise answer "no"'


def start_game():
    random = randomint()
    game_parts = {}
    game_parts['quest'] = random
    if random % 2 == 0:
        game_parts['true_answer'] = 'yes'
    else:
        game_parts['true_answer'] = 'no'
    return game_parts
