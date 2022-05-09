MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
#TODO: 1. Print report of all coffee machine resources


# count the money


# check resources sufficient?
def is_resources_enough(order_ingredients):
    """Returns True when resources are sufficient, False when there are insufficient resources"""

    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True
# process coins
def process_coins():
    """Returns the total number of coins inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters?"))* 0.25
    total += int(input("How many dimes?"))* 0.1
    total += int(input("How many nickles?"))* 0.05
    total += int(input("How many pennies?"))* 0.01
    return  total

def is_successful_transaction(amount, drink):
    if amount < drink['cost']:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        global money
        money += drink['cost']
        change = round(amount- drink['cost'],2) # returns the change
        print(f"Here is ${change} dollars in change.")
        return True

# update the resource list
def make_coffee(drink_name, order_ingredients):

    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")


money = 0
switch = True
while switch:
    choice = input("What would you like? (espresso/latte/cappucino):")
    # print report
    if choice == 'off':
        switch = False
    elif choice == 'report':
        print(str(resources["water"]) + 'ml')
        print(str(resources["milk"]) + 'g')
        print(str(resources["coffee"]) + 'ml')
        print("$" + str(money))
    else:
        # check transaction successful?
        drink = MENU[choice]

        if is_resources_enough(drink["ingredients"]):
            amount = process_coins()
            if is_successful_transaction(amount, drink):
                make_coffee(choice, drink['ingredients'])


