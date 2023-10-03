# Coffee Machine Simulation Program
'''This program is a simulation of a coffee machine.  The program asks the user to enter which
drink they want (espresso/latte/cappuccino).  It then asks the user to enter the coins they are paying with
and tracks whether they have entered enough and if so gives back change.  The program also is tracking
the amount of ingredients left in the coffee machine, each drink takes a different set of ingredients.
There are also two options for the maintenence team of the coffee machine "off" and "report".  "off" will just
end the program, turning the coffee machine off and "report" will print out the ingredients currently left
in the machine.'''

# import the ingredients and resources over from other file
from day15_importfile import *

# storing the ingredients in variables
water = resources['water']
milk = resources['milk']
coffee = resources['coffee']
money = 0

# storing ingredients of drinks in variables
espresso = menu['espresso']['ingredients']
latte = menu['latte']['ingredients']
cappuccino = menu['cappuccino']['ingredients']

# creating a dictionary for the prices of the drinks
prices_dict = {}
prices_dict['espresso'] = 1.50
prices_dict['latte'] = 2.50
prices_dict['cappuccino'] = 3.00

def turn_off_machine(order):
    if order == "off":
        machine_off = True
        return machine_off

def report(order):
    if order == "report":
        print(f"CURRENT_RESOURCES:\nWater: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g")


def resources_insufficient(order):
    if order == "espresso" and espresso['water'] > water:
        print("\nSorry, there is not enough water.")
        insufficient = True
        return insufficient
    if order == "espresso" and espresso['coffee'] > coffee:
        print("\nSorry, there is not enough coffee.")
        insufficient = True
        return insufficient
    if order == "latte" and latte['water'] > water:
        print("\nSorry, there is not enough water.")
        insufficient = True
        return insufficient
    if order == "latte" and latte['milk'] > milk:
        print("\nSorry, there is not enough milk.")
        insufficient = True
        return insufficient
    if order == "latte" and latte['coffee'] > coffee:
        print("\nSorry, there is not enough coffee.")
        insufficient = True
        return insufficient
    if order == "cappuccino" and cappuccino['water'] > water:
        print("\nSorry, there is not enough coffee.")
        insufficient = True
        return insufficient
    if order == "cappuccino" and cappuccino['milk'] > milk:
        print("\nSorry, there is not enough coffee.")
        insufficient = True
        return insufficient
    if order == "cappuccino" and cappuccino['coffee'] > coffee:
        print("\nSorry, there is not enough coffee.")
        insufficient = True
        return insufficient
    else:
        insufficient = False
        return insufficient


def process_coins(order, prices):

    order = str(order)
    profit = 0

    quarter_value = .25
    dime_value = .1
    nickel_value = .05
    penny_value = .01

    print("\nOK sure, please insert coins below to pay for your drink.")

    # Ask the customer what coins they are paying with.
    # Convert to integer data type
    quarters = int(input("\nHow many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    coins_inserted = (quarters * quarter_value) + (dimes * dime_value) + (nickels * nickel_value) + (pennies * penny_value)
    price = prices[order]

    change = round(coins_inserted - price, 2)

    if coins_inserted >= price:
        print(f"\nHere is ${change} in change....")
        print(f"\nYour {order} will be ready in just a couple minutes.\n...\n....\n.....")
        profit += price
        processed = True
        return profit, processed
    elif coins_inserted < price:
        print("\nSorry, that's not enough money.  Money refunded.")
        processed = False
        return profit, processed


def make_drink_one(order, ingredient1, ingredient2):

    print(f"\nHere is your {order} ☕.  Enjoy!")

    global water, coffee

    water -= espresso['water']
    coffee -= espresso['coffee']
    return water, coffee


def make_drink_two(order, ingredient1, ingredient2, ingredient3):

    print(f"\nHere is your {order} ☕.  Enjoy!")

    global water, milk, coffee

    if order == "latte":
        water -= latte['water']
        milk -= latte['milk']
        coffee -= latte['coffee']
    elif order == "cappuccino":
        water -= cappuccino['water']
        milk -= cappuccino['milk']
        coffee -= cappuccino['coffee']
    return water, milk, coffee


# Running the program
def run_machine():

    machine_on = True
    while machine_on == True:

        print("\n☕☕☕  Hello!  Welcome to our coffee machine.  ☕☕☕")

        customer_order = input("\nWhat would you like to order? (espresso/latte/cappucino)?: ").lower()

        if turn_off_machine(customer_order) == True:
            machine_on = False
            continue

        report(customer_order)

        if resources_insufficient(customer_order) == True and customer_order != "report":
            print("\nPlease wait one moment while we refill the coffee machine.  Thank you.")
            machine_on = False
            continue
        if customer_order != "report" and resources_insufficient(customer_order) == False and process_coins(customer_order, prices_dict)[1] == True:

            if customer_order == "espresso":
                make_drink_one(customer_order, water, coffee)
            elif customer_order == "latte" or customer_order == "cappuccino":
                make_drink_two(customer_order, water, milk, coffee)


run_machine()

