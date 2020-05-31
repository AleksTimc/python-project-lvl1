from brain_games.cli import answer
from brain_games.cli import randomint
from sympy import isprime


def is_prime():
    random = randomint()
    print('Question: ' + str(random))
    quest_answer = answer()
    final = []
    if isprime(random) is True and \
        quest_answer == 'yes' \
        or isprime(random) is False \
            and quest_answer == 'no':
        return True
    else:
        final.append(quest_answer)
        if isprime(random) is True:
            final.append('yes')
        else:
            final.append('no')
        return final
