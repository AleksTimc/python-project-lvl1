from brain_games.cli import welcome_user, greet
from brain_games.games.brain_calc import brain_calc
from brain_games.games.brain_even import even_game


def round_calc():
    greet()
    print('What is the result of the expression?')
    name = welcome_user()
    attempt = 0
    while attempt < 3:
        result = brain_calc()
        if result is True:
            print('Correct!')
            attempt = attempt + 1
        else:
            print(str(result[0]) + " is wrong answer ;(."
                  "Correct answer was " + str(result[1]) + ".")
            print("Let's try again," + name)
            break
    if attempt == 3:
        print('Congratulations, ' + name)


def round_even():
    greet()
    print('Answer "yes" if number even otherwise answer "no"')
    name = welcome_user()
    attempt = 0
    while attempt < 3:
        result = even_game()
        if result is True:
            print('Correct!')
            attempt = attempt + 1
        else:
            print(str(result[0]) + " is wrong answer ;(."
                  "Correct answer was " + str(result[1]) + ".")
            print("Let's try again," + name)
            break
    if attempt == 3:
        print('Congratulations, ' + name)


def main():
    round_calc()


def sec():
    round_even()


if __name__ == '__main__':
    main()
