import random
import os
import art
from game_data import data

count_score = 0
AA = random.choice(data)
BB = random.choice(data)

def compare(X, Y, Z):
    global count_score
    global AA
    global BB
    if (X > Y and Z == "A") or (Y > X and Z =="B"):
        AA = BB
        BB = random.choice(data)
        count_score += 1
        os.system('clear')
        print(art.logo)
        print(f"You're are right! Current Score: {count_score}")
        repeat(AA,BB)
    else:
        print(f"Sorry, that's wrong. Final score: {count_score}")

def repeat(AA,BB):
    while AA == BB:
        BB = random.choice(data)
    print(f"Compare A: {AA['name']}, a {AA['description']}, from {AA['country']}.")
    print(art.vs)
    print(f"Against B: {BB['name']}, a {BB['description']}, from {BB['country']}.")
    user_input = input("Who has more followers? Type 'A' or 'B': ")
    compare(X = AA['follower_count'], Y = BB['follower_count'], Z = user_input)

print(art.logo)
repeat(AA,BB)
