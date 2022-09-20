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

cost_of_espresso = MENU["espresso"]["cost"]
cost_of_latte = MENU["latte"]["cost"]
cost_of_cappuccino = MENU["cappuccino"]["cost"]

water_esp = MENU['espresso']['ingredients']['water']
milk_esp = MENU['espresso']['ingredients']['water']
coffee_esp = MENU['espresso']['ingredients']['water']

water_latte = MENU['latte']['ingredients']['water']
milk_latte = MENU['latte']['ingredients']['water']
coffee_latte = MENU['latte']['ingredients']['water']

water_cap = MENU['cappuccino']['ingredients']['water']
milk_cap = MENU['cappuccino']['ingredients']['water']
coffee_cap = MENU['cappuccino']['ingredients']['water']





water_of_resources = resources['water']
milk_of_resources = resources['milk']
coffee_of_resources = resources['coffee']

done = True

# while done:
# ask = input(f"What would you like? (espresso/latte/cappuccino): ").lower()
#  if ask == 'report':
#      print(f'Water: {resources["water"]}')
#  elif ask == 'espresso':
#      if water_of_resources < water_esp or milk_of_resources < milk_esp or coffee_of_resources < coffee_esp:
#          print(f"Sorry, there is not enough ")
#      else:
#           print(f"Please insert coins + '\n' + {int(input('How many dimes?: '))*0.25} + '\n' + {int(input('How many quarters?: '))*0.10} + '\n' + {int(input('How many nickels?: '))*0.05} + '\n' + {int(input('How many pennies?: '))*0.01}")
#        if money_inserted < cost_of_espresso:
#     print("Sorry, that's not enough money. Money refunded.")
# elif money_inserted == cost_of_espresso:
#   print("Here is your coffee, enjoy!")
##    water_of_resources -= water_esp
#     milk_of_resources -= milk_esp
#      coffee_of_resources -= coffee_esp
#   else:
#        print(f"Here is your {money_inserted - cost_of_espresso} in change.")
#         print("Here is your coffee, enjoy!")
#          water_of_resources -= water_esp
#           milk_of_resources -= milk_esp
#            coffee_of_resources -= coffee_esp

def is_order_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True
            

def process_coins():
    print("Please insert coins. ")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is {change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ")







profit = 0
while done:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == 'off':
        done = False
    elif choice == 'report':
        print(f'Water: {resources["water"]}')
        print(f'Milk: {resources["milk"]}')
        print(f'Coffee: {resources["coffee"]}')
        print(f'Money: {profit}')
    else:
        drink = MENU[choice]
        if is_order_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])

