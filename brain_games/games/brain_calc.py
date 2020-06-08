from brain_games.cli import randomint, rand_operator


INSTRUCTION = 'What is the result of the expression?'


def start_game():
    num_one = randomint()
    num_two = randomint()
    oper = rand_operator()
    game_parts = {}
    game_parts['quest'] = str(num_one) + ' ' + oper + ' ' + str(num_two)
    if oper == '*':
        game_parts['true_answer'] = num_one * num_two
    elif oper == '-':
        game_parts['true_answer'] = num_one - num_two
    else:
        game_parts['true_answer'] = num_one + num_two
    return game_parts
