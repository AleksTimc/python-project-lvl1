import prompt


def game_engine(game):
    print('Welcome to the Brain Games!')
    print(game.INSTRUCTION)
    print()
    name = prompt.string('May I have your name? ')
    print("Hello, {}!". format(name))
    rounds_count = 3
    attempt = 0
    while attempt < rounds_count:
        question, true_answer = game.generate_data()
        print('Question: ' + str(question))
        answer = prompt.string('Your answer: ')
        if answer == true_answer:
            print('Correct!')
            attempt += 1
        else:
            print(str(answer) + " is wrong answer ;(."
                  "Correct answer was " + str(true_answer) + ".")
            print("Let's try again, " + name)
            return
    print('Congratulations, ' + name)
