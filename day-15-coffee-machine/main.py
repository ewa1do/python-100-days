from copy import deepcopy

from data import MENU, resources

resources_copy = deepcopy(resources)
cash_money = 0

def what_would_you_like():
    valid_choices = ["espresso", "latte", "cappuccino", "report"]

    choice = input("What would you like? (espresso/latte/cappuccino):")

    while choice not in valid_choices:

        if choice == "off":
            print("Power off...")
            break

        print("Invalid choice!")
        choice = input("What would you like? (espresso/latte/cappuccino):")

    return choice

def print_report(resources=resources_copy):
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]

    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}ml\n{f"${cash_money}" if cash_money > 0 else ""}")

def print_not_enough(ingredient):
    print(f"Sorry there is not enough {ingredient}.")

def are_enough_resources(choice, resources=resources_copy):
    coffee_choice = MENU[choice]

    enough_water = resources["water"] >= coffee_choice["ingredients"]["water"]

    if not enough_water:
        print_not_enough("water")
        return False

    enough_coffee = resources["coffee"] >= coffee_choice["ingredients"]["coffee"]

    if not enough_coffee:
        print_not_enough("coffee")
        return False

    # enough_milk = True

    if "milk" in coffee_choice["ingredients"]:
        enough_milk = resources["milk"] >= coffee_choice["ingredients"]["milk"]

        if not enough_milk:
            print_not_enough("milk")
            return False

    return True

def process_coins():
    coins = { "quarters": 0.25, "dimes": 0.10, "nickles": 0.05, "pennies": 0.01 }

    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    return (quarters * coins["quarters"]) + (dimes * coins["dimes"]) + (nickles * coins["nickles"]) + (pennies * coins["pennies"])

def is_transaction_successful(money, coffee):

    coffe_cost = coffee["cost"]

    if money < coffe_cost:
        print("Sorry that's not enough money. Money refunded")
        return False

    if money >= coffe_cost:
        print("Enjoy your coffee :)")

        global resources_copy

        for ingredient in coffee["ingredients"]:
            resources_copy[ingredient] -= coffee["ingredients"][ingredient]


        global cash_money
        cash_money += round(money, 2)

        spare_change = round(money - coffe_cost, 2)

        if spare_change:
            print(f"Here's ${spare_change} dollar in change.")

        return True

def coffee_machine():
    while True:
        user_prompt = what_would_you_like()

        if user_prompt == "off":
            return

        if user_prompt == "report":
            print_report()
            continue

        if not are_enough_resources(user_prompt): return

        user_money = process_coins()

        is_transaction_successful(user_money, MENU[user_prompt])

coffee_machine()
