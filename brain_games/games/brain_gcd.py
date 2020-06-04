from brain_games.cli import randomint


def brain_gcd():
    num_one = randomint()
    num_two = randomint()
    game_parts = {}
    game_parts['instruction'] = 'Find the greatest common' \
                                'divisor of given numbers.'
    game_parts['quest'] = str(num_one) + ' ' + str(num_two)
    while num_one != 0 and num_two != 0:
        if num_one > num_two:
            num_one = num_one % num_two
        else:
            num_two = num_two % num_one
        game_parts['true_answer'] = num_one + num_two
    return game_parts
