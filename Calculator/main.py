import os
from art import logo
result = 0
store = []
def calculator(F,S,O):
    if O == "+":
        result = F+S
    elif O == "-":
        result = F-S
    elif O == "*":
        result = F*S
    elif O == "/":
        result = F/S
    return result
def start():
    print(logo)
    first = float(input("What's the first number?: "))
    xyz = True
    while xyz:
        operation = input("+\n-\n*\n/\nPick an operation: ")
        second = float(input("What's the second number?: "))
        temp_result = calculator(F=first,S=second,O=operation)
        print(f"{first} {operation} {second} = {temp_result}")
        again = input(f"Type 'y' to continue with {temp_result}, or type 'n' to start a new calculation: ")
        if again == "n":
            os.system('clear')
            xyz = False
        if again == "y":
            first = temp_result
    start()
start()