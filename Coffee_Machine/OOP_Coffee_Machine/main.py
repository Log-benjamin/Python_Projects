from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
My_coffee_machine = CoffeeMaker()
My_cash_register = MoneyMachine()
start = True

while start:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        start = False
    elif choice == "report":
        My_coffee_machine.report()
        My_cash_register.report()
    else:
        drink = menu.find_drink(choice)
        enough = My_coffee_machine.is_resource_sufficient(drink)
        if enough:
            My_cash_register.make_payment(drink.cost)
            My_coffee_machine.make_coffee(drink)
