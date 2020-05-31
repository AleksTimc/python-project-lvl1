from brain_games.cli import welcome_user, greet
from brain_games.games.brain_calc import brain_calc
from brain_games.games.brain_even import even_game
from brain_games.games.brain_gcd import brain_gcd
from brain_games.games.brain_progressive import progressive


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


def round_gcd():
    greet()
    print('Find the greatest common divisor of given numbers.')
    name = welcome_user()
    attempt = 0
    while attempt < 3:
        result = brain_gcd()
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


def round_progressive():
    greet()
    print('What number is missing in the progression?')
    name = welcome_user()
    attempt = 0
    while attempt < 3:
        result = progressive()
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


def gcd_game():
    round_gcd()


def progressive_game():
    round_progressive()


if __name__ == '__main__':
    main()
