from brain_games.cli import answer, randomint, is_number


def brain_gcd():
    num_one = randomint()
    num_two = randomint()
    score = 0
    print('Question: ' + ' ' + str(num_one) + ' ' ' ' + str(num_two))
    quest_answer = answer()
    final = []
    while num_one != 0 and num_two != 0:
        if num_one > num_two:
            num_one = num_one % num_two
        else:
            num_two = num_two % num_one
        score = num_one + num_two
    if is_number(str(quest_answer)) is False:
        final.append(str(quest_answer))
        final.append(str(score))
        return final
    if int(quest_answer) == score:
        return True
    else:
        final.append(str(quest_answer))
        final.append(str(score))
        return final
