import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    guess = None
    chances = 0
    while (guess != number_to_guess):
        if chances < 5:
            guess = int(input("Guess a number between 1 and 100: "))
            if guess < number_to_guess:
                chances = chances + 1
                print("Too low!")
            elif guess > number_to_guess:
                chances = chances + 1
                print("Too high!")
        else:
            print("Chances Over")
            break
    if chances < 5 :
        print("Congratulations! You guessed the number.")

number_guessing_game()