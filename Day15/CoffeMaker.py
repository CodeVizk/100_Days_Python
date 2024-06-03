MENU = {
    "espresso": {
        "ingredients": {
            "water": 60,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(order_ingredient):
    """Returns True when order can be made, and False when not."""
    for items in resources:
        if resources[items] >= order_ingredient[items]:
            return True
        else:
            print(f"Sorry, there is not enough {items}")
            return False


def coin_process():
    """Returns the total calculated coins inserted"""
    total_money = 0
    print("Please insert coins.")
    total_money += int(input("How many quarters? "))*0.25
    total_money += int(input("How many dimes? "))*0.10
    total_money += int(input("How many nickles? "))*0.05
    total_money += int(input("How many pennies? "))*0.01
    return total_money

def make_coffee(drink,order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink} ☕️. Enjoy!")

def is_transaction_successful(money_received ,drink_cost ):
    """Returns True when payment is accepted or False if money is insufficient. """
    if money_received>=drink_cost:
        change=round(money_received-drink_cost,2)
        print(f"Here is ${change} in change.")
        global profit
        profit+=drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False
turn_off = False
while not turn_off:
    User_drink = input("What would you like? (espresso, latte, cappuccino) or get(report) ")
    if User_drink == "report":
        print(
            f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: {profit}")
    elif User_drink == "off":
        turn_off = True
    else:
        choice = MENU[User_drink]
        if check_resources(order_ingredient=choice["ingredients"]):
            payment=coin_process()
            if is_transaction_successful(money_received=payment,drink_cost=choice["cost"]):
                make_coffee(User_drink,choice["ingredients"])



