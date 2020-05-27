from brain_games.cli import answer, randomint, rand_operator, is_number


def brain_calc():
    num_one = randomint()
    num_two = randomint()
    oper = rand_operator()
    score = 0
    print('Question: ' + ' ' + str(num_one) + ' ' + oper + ' ' + str(num_two))
    quest_answer = answer()
    final = []
    if oper == '*':
        score = score + num_one * num_two
    elif oper == '-':
        score = score + num_one - num_two
    else:
        score = score + num_one + num_two
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


def main():
    brain_calc()


if __name__ == '__main__':
    main()
