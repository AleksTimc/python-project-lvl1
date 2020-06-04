from brain_games.cli import game_engine2
from brain_games.games.brain_calc import brain_calc
from brain_games.games.brain_even import even_game
from brain_games.games.brain_gcd import brain_gcd
from brain_games.games.brain_progressive import progressive
from brain_games.games.is_prime import is_prime


def main():
    game_engine2(brain_calc)


def sec():
    game_engine2(even_game)


def progressive_game():
    game_engine2(progressive)


def gcd_game():
    game_engine2(brain_gcd)


def is_prime_game():
    game_engine2(is_prime)


if __name__ == '__main__':
    main()
