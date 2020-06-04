from brain_games.cli import randomint, rand_operator


def brain_calc():
    num_one = randomint()
    num_two = randomint()
    oper = rand_operator()
    game_parts = {}
    game_parts['instruction'] = 'What is the result of the expression?'
    game_parts['quest'] = str(num_one) + ' ' + oper + ' ' + str(num_two)
    if oper == '*':
        game_parts['true_answer'] = num_one * num_two
    elif oper == '-':
        game_parts['true_answer'] = num_one - num_two
    else:
        game_parts['true_answer'] = num_one + num_two
    return game_parts


def main():
    brain_calc()
