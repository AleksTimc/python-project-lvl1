from brain_games.cli import randomint


def even_game():
    random = randomint()
    game_parts = {}
    game_parts['instruction'] = 'Answer "yes" if given number' \
                                ' is prime. Otherwise answer "no"'
    game_parts['quest'] = random
    if random % 2 == 0:
        game_parts['true_answer'] = 'yes'
    else:
        game_parts['true_answer'] = 'no'
    return game_parts


def sec():
    print(even_game())
