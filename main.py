from random import randint

EASY_LEVEL_TURN = 10
HARD_LEVEL_TURN= 5



def check_answer(user_guess, actual_answer, turns):
    if user_guess >actual_answer:
        print("too high")
        return turns -1
    elif user_guess < actual_answer:
        print("too low")
        return turns -1
    else:
        print(f"you guess the answer{actual_answer}")

def set_difficulty():
    level = input("choose a difficulty , type 'easy' or  'hard'" )
    if level == "easy":
        return EASY_LEVEL_TURN
    else:
        return HARD_LEVEL_TURN


def game():
    print("welcome to the guessing game")
    guess = input("im thinking of a number between 1 and 100")
    answer = randint(1, 100)
    print(f"the answer is {answer}")

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"you still have {turns} attempts remaining to guess")

        guess = int(input("make a guess"))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("you have low out of turns you fail ")
            return
        elif guess != answer:
            print("guess again  ")
        else:
            return "come back and play"

game()