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

def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"sorry not enough {item}")
            return False
    return True


def process_coins():
    print("please insert coins")
    total = int(input("how many quarters?:"))*0.25
    total +=int(input("how many dimes?:"))*0.10
    total +=int(input("how many nickel?"))*0.05
    total +=int(input("how many pennies?:"))*0.01
    return total

def is_transaction_succesful(money_received,drink_cost):
    if money_received > drink_cost:
        change = round(money_received- drink_cost,2)
        print(f"here's the change {change}")
        global profit
        profit +=drink_cost
        return True
    else:
        print("sorry that's not enough money.money refunded")
        return False     

def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"here is your {drink_name},enjoy!")    

is_on = True

while is_on:
    choice= input("what would you like (espresso/latte/cappuccino):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water : {resources['water']} ml")
        print(f"milk : {resources['milk']} ml")
        print(f"coffee : {resources['coffee']} ml")
        print(f"money: ${profit}")  
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_succesful(payment,drink["cost"]):
                make_coffee(choice, drink["ingredients"])
        