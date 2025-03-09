import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

symbol_count = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}

def check_winning(columns, lines, bet, values):
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
        for i in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

def get_deposit():
    while True: 
        amount = input("Enter the amount you want to deposit ($): ")
        if amount.isdigit():
            amount = int(amount)
            if amount < 0:
                print("Deposit amount must be more than $0.")
        else:
            print("Please enter a valid number.")
        return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines you want to bet on (1-" + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter a valid number of lines.")
        else:
            print("Please enter a valid number.")
    return lines

def get_bet():
    while True:
        bet = input("Enter the amount you would like to bet on each line ($): ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Betting amount must be between {MIN_BET} and {MAX_BET}.")
        else:
            print("Please enter a valid number.")
    return bet

def spin(balance):
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"You don't have enough money to make this bet, your balance is ${balance}.")
            play = input("Type 'add' to add more money or 'q' to quit: ")
            if play == "add":
                balance += get_deposit()
                print(f"Your new balance is ${balance}.")
            elif play == "q":
                return 0
        else:
            break
    print(f"You're betting ${bet} on {lines} lines, Total bet is equal to: ${total_bet}.")
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winning(slots, lines, bet, symbol_count)

    if winnings > 0:
        print(f"Congratulations! You won ${winnings} on lines {winning_lines}.")
    else:
        print("You lost the bet")
    return winnings - total_bet

def main():
    balance = get_deposit()
    while True:
        print(f"Your current balance is ${balance}.")
        play = input("Press enter to play or 'add' to add more money to your balance or 'q' to exit: ")
        if play == "q":
            break
        elif play == "add":
            balance += get_deposit()
        elif play == "":
            balance += spin(balance)
    print(f"Your final balance is ${balance}.")
    print("Thanks for playing!")

main()