from art import coffee_logo
import os


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

def add_money(x):
    resources['money'] = x

def print_resources():
    print(f"\nWater: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${resources['money']}\n")

def check_resources(coffee):
    
    coffee_ingredients = MENU[coffee]['ingredients']
    water_needed = coffee_ingredients['water']
    water = resources['water']
    coffee_needed = coffee_ingredients['coffee']
    coffee_grounds = resources['coffee']

    if water_needed > water :
            print('Sorry there is not enough water.')
            return False
    elif coffee_needed > coffee_grounds:
            print('Sorry there is not enough coffee.')
            return False
    
    elif coffee != 'espresso':
        milk_needed = coffee_ingredients['milk']
        milk = resources['milk']
        
        if milk_needed > milk:
            print('Sorry there is not enough milk.')
            return False
        else:
            return True
    else:
        return True    

def add_coins(inserted_coins):
    total = 0
    for coin in inserted_coins:
        if coin == 'q':
            total += 0.25
        elif coin == 'd':
            total += 0.10
        elif coin == 'n':
            total += 0.05
        elif coin == 'p':
            total += 0.01

    return total

def process_transaction(money, coffee_type):
    money_needed = MENU[coffee_type]['cost']
    
    if money < money_needed:
        print(f"Sorry that's not enough money. Cost is ${money_needed}. Money refunded.")
        return False
    elif money == money_needed:
        print("Transaction succesful.")
        add_money(money)
        return True
    else:
        change = money - money_needed
        add_money(money_needed)
        print(f'Here is ${change} dollars in change.')
        return True

def deduct_ingredients(coffee_type):
    coffee_ingredients = MENU[coffee_type]['ingredients']
    water_used = coffee_ingredients['water']      
    coffee_used = coffee_ingredients['coffee']
    if coffee_type != 'espresso':
        milk_used = coffee_ingredients['milk']
        resources['milk'] -= milk_used 

    resources['coffee'] -= coffee_used
    resources['water'] -= water_used


    


resources['money'] = 0
order_again = 'yes'

while order_again == 'yes':
    
    print(coffee_logo)
    coffee = input("Here is our menu:\n - Espresso\n - Latte\n - Cappuccino\nWhat would you like? ").lower()

    if coffee == 'off':
        quit()
    elif coffee == 'report':
        print_resources()
        continue
    elif coffee == 'espresso' or coffee == 'cappuccino' or coffee == 'latte':
        enough_resources = check_resources(coffee)
        if enough_resources:
            inserted_coins = input("Insert coins one at a time (q/d/n/p) : ").split()
            money = add_coins(inserted_coins)
            transaction_processed = process_transaction(money, coffee)
            if transaction_processed:
                deduct_ingredients(coffee)
                print(f"Here is your {coffee}. Enjoy!")
            else:
                order_again = input("Transaction failed. Do you want to order another drink? Type 'yes' or 'no' : ").lower()
                continue
        else:
            order_again = input("Do you want to order another drink? Type 'yes' or 'no' : ").lower()
            continue
    else:
        print("That's not a valid option.")
        order_again = input("Do you want to order another drink? Type 'yes' or 'no' : ").lower()
        continue
    