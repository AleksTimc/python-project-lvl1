import random


INSTRUCTION = 'What number is missing in the progression?'


def generate_data():
    start_number = random.randint(1, 50)
    step_number = random.randint(1, 10)
    progression_lenght = 10
    step_for_quest = random.randint(0, progression_lenght-1)
    end_number = step_number * progression_lenght + start_number
    progression_list = list(range(start_number, end_number, step_number))
    true_answer = progression_list[step_for_quest]
    progression_list[step_for_quest] = '..'
    progression_quest = ' '.join(str(element) for element in progression_list)
    return progression_quest, true_answer
