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

ask = input(f"What would you like? (espresso/latte/cappuccino): ").lower()
if ask == 'report':
    print(f'Water: {resources["water"]}')
elif ask == 'espresso':
    if water_esp < water_of_resources or milk_esp < milk_of_resources or coffee_esp < coffee_of_resources:
        print(f"Sorry, there is not enough ")
    elif print("Please insert coins.")