# TODO: The types of coffee and resources.
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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

money = 0
current_resource = resources


# TODO: 2. print the resource to the user.


def resource(ingre):
    print(f"Water: {ingre['water']}ml")
    print(f"Milk: {ingre['milk']}")
    print(f"Coffee: {ingre['coffee']}")
    print(f"Money: {money}")
    return


# TODO: 3. Check the resource if sufficient resource return true.

def check_resource(total_resource, needed_resource):
    for item in total_resource:
        if total_resource[item] <= needed_resource[item]:
            print(f"Sorry not enough resource {item}")
            return False
    return True


# TODO: 4. Coin processing

def coins_process(item_money):
    quarters = int(input("How many quarters: ")) * 0.25
    dimes = int(input("How many dimes: ")) * 0.10
    nickles = int(input("How many nickles: ")) * 0.05
    pennies = int(input("How many pennies: ")) * 0.01
    total_money = quarters + dimes + nickles + pennies
    return total_money


# TODO: 5. Remove the resource.


def resource_process(total_resource, needed_resource):
    left_resource = {}
    for item in total_resource:
        left_resource[item] = total_resource[item] - needed_resource[item]
    return left_resource


should_continue = True

while should_continue:
    command = input("What would you like? (espresso, latte, cappuccino) ").lower()
    if command == "off":
        should_continue = False
        print("Sorry the machine is out of service!!")
    elif command == "report":
        print(resource(current_resource))
    else:
        item_resource = MENU[command]["ingredients"]
        item_cost = MENU[command]["cost"]
        if check_resource(current_resource, item_resource):
            money = coins_process(item_cost)
            if money > item_cost:
                remaining_money = money - item_cost
                print(f"Here is your change: {remaining_money}")
                current_resource = resource_process(current_resource, item_resource)
                print(f"Here is your {command}.")
            else:
                print("Sorry that is not enough money. Money Refund.")
