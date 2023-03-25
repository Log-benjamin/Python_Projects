from menu import MENU


state = True

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def check_stock(u):
    if resources['water'] - MENU[u]['ingredients']['water'] < 0:
        print("Sorry there is not enough water.")
        return False
    elif resources['milk'] - MENU[u]['ingredients']['milk'] < 0:
        print("Sorry there is not enough milk.")
        return False
    elif resources['coffee'] - MENU[u]['ingredients']['coffee'] < 0:
        print("Sorry there is not enough coffee.")
        return False
    else:
        return True


def make_coffee(elc, q, d, n, p):
    cash = (q * 0.25) + (d * 0.1) + (n * 0.05) + (p * 0.01)
    change = round(cash - MENU[elc]['cost'], 2)
    resources['water'] = resources['water'] - MENU[elc]['ingredients']['water']
    resources['milk'] = resources['milk'] - MENU[elc]['ingredients']['milk']
    resources['coffee'] = resources['coffee'] - MENU[elc]['ingredients']['coffee']
    resources['money'] = resources['money'] + MENU[elc]['cost']
    if change >= 0:
        print(f"Here is ${change} in change. \nHere is your {elc} ☕  Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")


# TODO: 1. Print a report of the coffee machine resources
while state:
    user: str = input("What would you like? (espresso/latte/cappuccino or report): ")
    if user == "report":
        print(f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee: {resources['coffee']}g \nMoney: ${resources['money']}")
    else:
        if check_stock(u=user):
            print("Please insert coins.")
            get_quarters: int = int(input("How many quarters?: "))
            get_dimes: int = int(input("How many dimes?: "))
            get_nickles: int = int(input("How many nickles?: "))
            get_pennies: int = int(input("How many pennies?: "))
            make_coffee(elc=user, q=get_quarters, d=get_dimes, n=get_nickles, p=get_pennies)
