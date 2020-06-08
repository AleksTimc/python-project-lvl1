from brain_games.cli import randomint
import random


INSTRUCTION = 'What number is missing in the progression?'


def randstep_quest():
    randstep_quest = random.randint(0, 9)
    return randstep_quest


def randstep():
    randstep = random.randint(1, 10)
    return randstep


def progression_data(start_number):
    step_number = randstep()
    end_number = step_number * 10 + start_number
    step_for_quest = randstep_quest()
    quest = list(range(start_number, end_number, step_number))
    quest2 = list(range(start_number, end_number, step_number))
    quest2[step_for_quest] = '..'
    quest_str = ' '.join(str(element) for element in quest2)
    true_answer = quest[step_for_quest]
    return quest_str, true_answer


def start_game():
    num_one = randomint()
    game_parts = {}
    game_parts['quest'], game_parts['true_answer'] = progression_data(num_one)
    return game_parts
