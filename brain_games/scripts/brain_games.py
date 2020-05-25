from brain_games.cli import welcome_user


def greet():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no"')
    print()


def main():
    greet()
    print()
    welcome_user()


if __name__ == '__main__':
    main()
