from brain_games.cli import welcome_user
from brain_games.cli import answer
from brain_games.scripts.brain_games import greet


greet()
gamer_name = welcome_user()


def even_game():
    result = 0
    while result < 3:
        import random
        random = random.randint(1, 50)
        print('Question: ' + str(random))
        quest_answer = answer()
        print(quest_answer)
        is_even = random % 2
        if is_even == 0 and \
            quest_answer == 'yes' \
            or is_even == 1 and \
                quest_answer == 'no':
            print('Correct!')
            result = result + 1
        else:
            if is_even == 1:
                print(quest_answer + " is wrong answer ;(."
                      "Correct answer was 'no'.")
            else:
                print(quest_answer + " is wrong answer ;(."
                      "Correct answer was 'yes'.")
            print("Let's try again, " + gamer_name)
            break
    if result == 3:
        print('Congratulations, ' + gamer_name + '!')


def main():
    even_game()


if __name__ == '__main__':
    main()
