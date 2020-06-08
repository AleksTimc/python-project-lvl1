from brain_games.cli import randomint, randstep, randstep_quest


INSTRUCTION = 'What number is missing in the progression?'


def start_game():
    step = randstep()
    step_for_quest = randstep_quest()
    num_one = randomint()
    num_two = step * 10 + num_one
    quest = list(range(num_one, num_two, step))
    quest2 = list(range(num_one, num_two, step))
    quest2[step_for_quest] = '..'
    quest_str = ' '.join(str(element) for element in quest2)
    game_parts = {}
    game_parts['quest'] = quest_str
    game_parts['true_answer'] = quest[step_for_quest]
    return game_parts
