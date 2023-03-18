import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)
again = ""
def display():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text=text, shift=shift, direction=direction)

def caesar(text, shift, direction):
    word = ""
    if shift > 25:
        shift %= 26
    for letter in text:
        if letter in alphabet:
            if direction == "encode":
                I = alphabet.index(letter) + shift
                if I > 25:
                    I -= 26
            elif direction == "decode":
                I = alphabet.index(letter) - shift
                if I < 0:
                    I += 26
            word += alphabet[I]
        else:
            word += letter
    print(f"The {direction}ed text is {word}")
display()
again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
if again == "no":
    print("Good Bye") 
while again == "yes":
    display()
    again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if again == "no":
        print("Good Bye")