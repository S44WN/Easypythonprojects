from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffeeMaker = CoffeeMaker()
menu = Menu()

is_on = True

money_machine.report()
coffeeMaker.report()

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        money_machine.report()
        coffeeMaker.report()
    else:
        drink = menu.find_drink(choice)
        if coffeeMaker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffeeMaker.make_coffee(drink)
