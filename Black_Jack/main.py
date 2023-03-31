from art import logo
import random
import os


def winner(user, computer):
    if user > 21 and computer > 21:
        return "You went over. You lose"
    if user == computer:
        return "Draw"
    elif computer == 0:
        return "Lose, opponent has Blackjack"
    elif user == 0:
        return "Win with a Blackjack"
    elif user > 21:
        return "You went over. You Lose"
    elif computer > 21:
        return "Opponent went over. You win"
    elif user > computer:
        return "You Win!"
    else:
        return "You Lose."

def get_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    return random.choice(cards)

def score(card):
    if sum(card) == 21 and len(card) == 2:
        return 0
    if 11 in card and sum(card) > 21:
        card.remove(11)
        card.append(1)  
    return sum(card)

def play():
    game_on = True
    print(logo)
    user_card = []
    computer_card = []
    for _ in range(2):
        user_card.append(get_card())
        computer_card.append(get_card())

    while game_on:
        user_score = score(user_card)
        computer_score = score(computer_card)
        print(f"Your cards: {user_card}, current score: {user_score}")
        print(f"Computer's first card: {computer_card[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_on = False
        else:
            user_deal = input("Type 'y' to get anothe card, type 'n' to pass: ")
            if user_deal == "y":
                user_card.append(get_card())
            else:
                game_on = False

    while computer_score !=0 and computer_score < 17:
        computer_card.append(get_card())
        computer_score = score(computer_card)
    
    print(f" Your final hand is: {user_card}, final score: {user_score}")
    print(f" Computer's final hand: {computer_card}, final score: {computer_score}")
    print(f" {winner(user_score, computer_score)}")

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system("clear")
    play()
