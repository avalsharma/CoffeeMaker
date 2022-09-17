MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

change=0
def payment(user_choice):
    print("Please insert your coins")
    quarters = int(input("How Many Quarters?"))
    dimes = int(input("How Many Dimes?"))
    nickels = int(input("How Many Nickels?"))
    pennies = int(input("How Many Pennies?"))

    return (pennies*0.01) + (nickels*0.05) + (dimes*0.10) + (quarters*0.25) - MENU[user_choice]["cost"]

def order(user_choice):
    drink_ordered = MENU[user_choice]
    return drink_ordered["ingredients"]

def interface():
    user_choice = input("What would you like? (espresso/latte/cappuccino):")

    if user_choice == "report":
        print(f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee: {resources['coffee']}g ")
        interface()
    elif user_choice== "off":
        return

    for i in resources:
        resources[i]-=order(user_choice)[i]

    enough_resources=True

    for key in resources:
        if resources[key]<0:
            enough_resources=False

    if enough_resources==True:

        change=payment(user_choice)
        if change>=0:
            print(f"Here is your ${change} in change \nHere is your {user_choice} enjoy!")
        else:
            print("Sorry that's not enough money. Money Refunded")
        interface()
    else:
        print("Not Enough Resources")
        interface()

interface()