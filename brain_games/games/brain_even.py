from brain_games.cli import answer
from brain_games.cli import randomint


def even_game():
    random = randomint()
    print('Question: ' + str(random))
    quest_answer = answer()
    final = []
    if random % 2 == 0 and \
        quest_answer == 'yes' \
        or random % 2 == 1 and \
            quest_answer == 'no':
        return True
    else:
        final.append(quest_answer)
        if random % 2 == 1:
            final.append('no')
        else:
            final.append('yes')
        return final


def main():
    even_game()


if __name__ == '__main__':
    main()
