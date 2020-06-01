from brain_games.cli import welcome_user, greet, game_instruction
from brain_games.games.brain_calc import brain_calc
from brain_games.games.brain_even import even_game
from brain_games.games.brain_gcd import brain_gcd
from brain_games.games.brain_progressive import progressive
from brain_games.games.is_prime import is_prime


def game_engine(game):
    greet()
    game_instruction(game)
    name = welcome_user()
    rounds = 3
    attempt = 0
    while attempt < rounds:
        result = game()
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
    game_engine(brain_calc)


def sec():
    game_engine(even_game)


def gcd_game():
    game_engine(brain_gcd)


def progressive_game():
    game_engine(progressive)


def isprime_game():
    game_engine(is_prime)


if __name__ == '__main__':
    main()
