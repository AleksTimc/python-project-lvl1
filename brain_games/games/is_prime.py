from brain_games.cli import randomint


INSTRUCTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def start_game():
    random = randomint()
    game_parts = {}
    game_parts['quest'] = random
    for digit in range(2, random):
        if (random % digit) == 0:
            game_parts['true_answer'] = 'no'
            break
        elif (random // digit) == 1:
            game_parts['true_answer'] = 'yes'
            break
    return game_parts
