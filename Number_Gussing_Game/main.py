import random
from art import logo
correct_guess = False
actua_value = random.randint(1,100)

print(logo)

def get_guess():
    guess = int(input("Make a guess: "))
    return guess

def mode(level):
    global correct_guess
    if level == "hard":
        x = 5
    else:
        x = 10
    
    while x > 0:
        print(f"You have {x} attempts remaining to guess the number.")
        guss = get_guess()
        if guss > actua_value:
            print("Too high.")
        elif guss < actua_value:
            print("Too low.")  
        else:
            correct_guess = True
            x = 1
        if x > 1:
            print("Guess again.")
        x -= 1 
    if correct_guess:
        print(f"You Won, The answer was {actua_value}.")
    else:
        print("You've run out of guess, you lose.")

print(actua_value)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")

mode(difficulty_level)

    
