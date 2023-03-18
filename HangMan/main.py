import random
import hangman_art
from hangman_words import word_list

print(hangman_art.logo)
chosen_word = random.choice(word_list)
Display = []
lives = 6
count = 0
word_len = len(chosen_word)
end_game = False
for z in range(len(chosen_word)):
    Display += "_"
print(chosen_word)

while not end_game:
    guess = input("Guess a Letter: ")
    if guess in Display:
        print(f"You have already gussed {guess}")
    for position in range(word_len):
        letter = chosen_word[position]
        if letter == guess:
            Display[position] = guess
    
    if guess not in chosen_word:
        lives -= 1
        print(f"You gussed {guess}, that's not in the word. You lose a life")
        if lives == 0:
           end_game = True 
           print("You Lose.")
    
    print(f" ".join(Display))
    
    if "_" not in Display:
        end_game = True
        print("You Won.")

    
    print(hangman_art.stages[lives])    

    
