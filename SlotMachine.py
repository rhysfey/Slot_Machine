import random


#Constants to be able to use anywhere
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines




def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count): #_ is anonymous value
            all_symbols.append(symbol)

    columns = [] #we define our columns list
    for _ in range(cols): #we generate a column for every single column we have
        #below we are picking a random value
        column = []     #column is an empty list
        current_symbols = all_symbols[:]   #current symbols(what we can currently select from) is a copy of all_symbols
        for _ in range(rows):  #we loop through the number of value we need to generate which is = number of rows in slot machine
            value = random.choice(all_symbols)  #a value is random
            current_symbols.remove(value)  #remove value not to be picked again
            column.append(value)  #add value to our column

        columns.append(column)  #we add our column to the columns list

    return columns


#for printing the slot machine

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()

#function def something we can
#call to execute code
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        #isdigit tells us that the value is real (+ve)
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
              break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount


#Start of actual program

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" +str(MAX_LINES)+ ")? ")
        #(1-" +str(MAX_LINES)+ ") to include MAX_LINES in the string
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
              break
            else:
                print("Please enter a valid number of lines")
        else:
            print("Please enter a whole number.")
    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        #isdigit tells us that the value is real (+ve)
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
              break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a whole number.")
    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet



#everything done under main to be able to call it later


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press to enter to play (Q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}.")

main()

