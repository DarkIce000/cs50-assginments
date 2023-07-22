#function for getting get_cents
def get_cents():
    try:
        change_Owe = float(input("change owe: "))
        return change_Owe
    except:
        get_cents()

#calling cents for getting the input
cents = get_cents()

#functions for calculating coins
def calculate_quaters(cents):
    return int(cents / 25)
def calculate_dimes(cents):
    return int(cents / 10)
def calculate_nickels(cents):
    return int(cents / 5)
def calculate_pennies(cents):
    return int(cents / 1)

#calculating coins of each type
quaters = calculate_quaters(cents)
cents = cents - 25 * quaters
dimes = calculate_dimes(cents)
cents = cents - 10 * dimes
nickels = calculate_nickels(cents)
cents = cents - 5 * nickels
pennies = calculate_pennies(cents)
cents = cents - 1 * pennies

#calculating coins
coins = quaters + dimes + nickels + pennies
print(f"{coins}")