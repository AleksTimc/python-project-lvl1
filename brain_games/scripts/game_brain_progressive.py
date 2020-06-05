from brain_games.cli import game_engine2
from brain_games.games.brain_progressive import progressive


def main():
    game_engine2(progressive)


if __name__ == '__main__':
    main()
