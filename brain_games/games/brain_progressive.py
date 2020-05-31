from brain_games.cli import answer, randomint, randstep, randstep_quest


def progressive():
    step = randstep()
    step_for_quest = randstep_quest()
    num_one = randomint()
    num_two = step*10+num_one
    quest = list(range(num_one, num_two, step))
    quest2 = list(range(num_one, num_two, step))
    quest2[step_for_quest] = '..'
    print('Question: ', end="")
    print(*quest2, sep=" ")
    quest_answer = answer()
    final = []
    if quest_answer == str(quest[step_for_quest]):
        return True
    else:
        final.append(str(quest_answer))
        final.append(str(quest[step_for_quest]))
        return final
