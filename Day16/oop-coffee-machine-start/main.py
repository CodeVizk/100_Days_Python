from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


my_menu = Menu()
my_coffee = CoffeeMaker()
payment = MoneyMachine()

is_on = True
while is_on:
    options = my_menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        my_coffee.report()
        payment.report()
    else:
        drink = my_menu.find_drink(choice)
        if my_coffee.is_resource_sufficient(drink) and payment.make_payment(drink.cost):
            my_coffee.make_coffee(drink)
