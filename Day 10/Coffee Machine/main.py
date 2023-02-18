from menu import menu

resources = {
    "water": 500,
    "milk": 500,
    "coffee": 500,
    "Money": 0
}


def start():
    choice = input("What would you like to have?(espresso/latte/cappuccino): ")
    if choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        start()
    elif choice == "off":
        exit()
    if choice in menu:
        if menu[choice]["ingredients"]["water"] <= resources["water"] and menu[choice]["ingredients"]["milk"] <= resources["milk"] and menu[choice]["ingredients"]["coffee"] <= resources["coffee"]:
            total = 0
            print("Please insert coins.")
            money_in = int(input("How many quarters: "))
            total += money_in*0.25
            money_in = int(input("How many dimes: "))
            total += money_in*0.10
            money_in = int(input("How many nickels: "))
            total += money_in*0.05
            money_in = int(input("How many pennies: "))
            total += money_in*0.01

            if total >= menu[choice]["cost"]:
                # reducing resources accordingly
                resources["water"] -= menu[choice]["ingredients"]["water"]
                resources["milk"] -= menu[choice]["ingredients"]["milk"]
                resources["coffee"] -= menu[choice]["ingredients"]["coffee"]

                change = total - menu[choice]["cost"]
                change = round(change, 2)
                total = total - change
                total = round(total, 2)
                resources["Money"] += total
                if change != 0:
                    print(f"Here is ${change} in change.")
                print(f"Here is your {choice} ☕. Enjoy!")
                start()
            else:
                print("Sorry, that's not enough money. Money refunded.")
                start()
        else:
            if resources["water"] < menu[choice]["ingredients"]["water"]:
                less = "water"
            elif resources["milk"] < menu[choice]["ingredients"]["milk"]:
                less = "milk"
            else:
                less = "coffee"
            print(f"Sorry, there is no enough {less}.")
            start()
    else:
        print("Sorry, invalid option. Try again.")


start()
