import os
from art import logo
print(logo)
bids = {}
state = False
print("Welcome to the secret auction program.")
def get_max_bid():
    max_value = 0
    max_bidder =""
    for key in bids:
        if bids[key] > max_value:
            max_value = bids[key]
            max_bidder = key
    print(f"The winner is {max_bidder} with a bid of ${max_value}.")
while not state:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bids[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if other_bidders == "no":
        get_max_bid()
        state = True
    else:
        os.system('clear')


