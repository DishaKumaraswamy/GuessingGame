import random

EASY = 10
HARD = 5
cont = ""
def check_answer(user_guess, actual_guess,turns):
    if user_guess < actual_guess:
        if turns-1 !=0:
            print("Too low, Guess high")
        return turns-1
    elif user_guess > actual_guess:
        if turns - 1 != 0:
            print("Too high, Guess low")
        return turns-1
    else:
        print(f"You've guessed it right! The answer was {actual_guess} ")
        conti = input("Another game? Type 'yes' or 'no' ")
        if conti == 'yes':
            game()

def check_difficulty():
    choice = input("Choose. Type 'easy' or 'hard' : ")
    if choice == 'easy':
        return EASY

    else:
        return HARD

def game():
    print("Welcome to the Number Guessing Game!")
    turns = check_difficulty()
    print("I've chosen a number between 1 and 100, Your Turn! ")
    num = random.randint(1,100)

    user_in = 0
    while user_in != num:
        print(f"You have {turns} attempts left.")
        user_in = int(input("Make a guess "))
        turns = check_answer(user_in, num, turns)
        if turns == 0:
            print(f"Pssst, You've run out of attempts, You lose! The correct answer is {num} ")
            contu = input("Another game? Type 'yes' or 'no' ")
            if contu == 'yes':
                game()
            else:
                return


game()
