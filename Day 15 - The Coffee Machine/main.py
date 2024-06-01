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

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

is_on = True


def getReport():
    for key, value in resources.items():
        print(f"{key}: {value}")


def countCoins():
    print("Please insert the coins.")
    quarters = input("How many quarters?: ")
    dimes = input("How many dimes?: ")
    nickels = input("How many nickles?: ")
    pennies = input("How many pennies?: ")

    total = ((int(quarters) * 0.25) + (int(dimes) * 0.10) + (int(nickels) * 0.05) + (int(pennies) * 0.01))

    return total


while is_on:

    order = input("What would you like? (espresso/latte/capuccino): ")

    if order == "espresso":
        water = MENU["espresso"]["ingredients"]["water"]
        coffee = MENU["espresso"]["ingredients"]["coffee"]

        if resources["water"] < water:
            print("Sorry there is not enough water.")

        elif resources["coffee"] < coffee:
            print("Sorry there is not enough coffee.")

        else:
            currentCoins = countCoins()

            if currentCoins >= MENU["espresso"]["cost"]:
                print("Here is your espresso. Enjoy!")
                change = currentCoins - MENU["espresso"]["cost"]
                print(f"Here is {round(change, 2)} dollars in change.")
                profit += MENU["espresso"]["cost"]
                resources["water"] -= water
                resources["coffee"] -= coffee
            else:
                print("Sorry that's not enough money. Money refunded.")

    elif order == "latte":

        water = MENU["latte"]["ingredients"]["water"]
        coffee = MENU["latte"]["ingredients"]["coffee"]
        milk = MENU["latte"]["ingredients"]["milk"]

        if resources["water"] < water:
            print("Sorry there is not enough water.")
        elif resources["coffee"] < coffee:
            print("Sorry there is not enough coffee.")
        elif resources["milk"] < milk:
            print("Sorry there is not enough milk.")
        else:
            currentCoins = countCoins()

            if currentCoins >= MENU["latte"]["cost"]:
                print("Here is your latte. Enjoy!")
                change = currentCoins - MENU["latte"]["cost"]
                print(f"Here is {round(change, 2)} dollars in change.")
                profit += MENU["latte"]["cost"]
                resources["water"] -= water
                resources["coffee"] -= coffee
                resources["milk"] -= milk
            else:
                print("Sorry that's not enough money. Money refunded.")

    elif order == "cappuccino":
        water = MENU["cappuccino"]["ingredients"]["water"]
        coffee = MENU["cappuccino"]["ingredients"]["coffee"]
        milk = MENU["cappuccino"]["ingredients"]["milk"]

        if resources["water"] < water:
            print("Sorry there is not enough water.")
        elif resources["coffee"] < coffee:
            print("Sorry there is not enough coffee.")
        elif resources["milk"] < milk:
            print("Sorry there is not enough milk.")
        else:
            currentCoins = countCoins()

            if currentCoins >= MENU["cappuccino"]["cost"]:
                print("Here is your cappuccino. Enjoy!")
                change = currentCoins - MENU["cappuccino"]["cost"]
                print(f"Here is {round(change, 2)} dollars in change.")
                profit += MENU["cappuccino"]["cost"]
                resources["water"] -= water
                resources["coffee"] -= coffee
                resources["milk"] -= milk
            else:
                print("Sorry that's not enough money. Money refunded.")

    elif order == "off":
        is_on = False

    elif order == "report":
        getReport()
