from brain_games.cli import welcome_user, greet
from brain_games.games.brain_calc import brain_calc
from brain_games.games.brain_even import even_game
from brain_games.games.brain_gcd import brain_gcd
from brain_games.games.brain_progressive import progressive
from brain_games.games.is_prime import is_prime


def round_calc():
    greet()
    print('What is the result of the expression?')
    name = welcome_user()
    rounds = 3
    attempt = 0
    while attempt < rounds:
        result = brain_calc()
        if result is True:
            print('Correct!')
            attempt += 1
        else:
            print(str(result[0]) + " is wrong answer ;(."
                  "Correct answer was " + str(result[1]) + ".")
            print("Let's try again," + name)
            break
    if attempt == rounds:
        print('Congratulations, ' + name)


def round_even():
    greet()
    print('Answer "yes" if number even otherwise answer "no"')
    name = welcome_user()
    rounds = 3
    attempt = 0
    while attempt < rounds:
        result = even_game()
        if result is True:
            print('Correct!')
            attempt += 1
        else:
            print(str(result[0]) + " is wrong answer ;(."
                  "Correct answer was " + str(result[1]) + ".")
            print("Let's try again," + name)
            break
    if attempt == rounds:
        print('Congratulations, ' + name)


def round_gcd():
    greet()
    print('Find the greatest common divisor of given numbers.')
    name = welcome_user()
    rounds = 3
    attempt = 0
    while attempt < rounds:
        result = brain_gcd()
        if result is True:
            print('Correct!')
            attempt += 1
        else:
            print(str(result[0]) + " is wrong answer ;(."
                  "Correct answer was " + str(result[1]) + ".")
            print("Let's try again," + name)
            break
    if attempt == rounds:
        print('Congratulations, ' + name)


def round_progressive():
    greet()
    print('What number is missing in the progression?')
    name = welcome_user()
    rounds = 3
    attempt = 0
    while attempt < rounds:
        result = progressive()
        if result is True:
            print('Correct!')
            attempt += 1
        else:
            print(str(result[0]) + " is wrong answer ;(."
                  "Correct answer was " + str(result[1]) + ".")
            print("Let's try again," + name)
            break
    if attempt == rounds:
        print('Congratulations, ' + name)


def round_isprime():
    greet()
    print('Answer "yes" if given number is prime. Otherwise answer "no"')
    name = welcome_user()
    rounds = 3
    attempt = 0
    while attempt < rounds:
        result = is_prime()
        if result is True:
            print('Correct!')
            attempt += 1
        else:
            print(str(result[0]) + " is wrong answer ;(."
                  "Correct answer was " + str(result[1]) + ".")
            print("Let's try again," + name)
            break
    if attempt == rounds:
        print('Congratulations, ' + name)


def main():
    round_calc()


def sec():
    round_even()


def gcd_game():
    round_gcd()


def progressive_game():
    round_progressive()


def isprime_game():
    round_isprime()


if __name__ == '__main__':
    main()
