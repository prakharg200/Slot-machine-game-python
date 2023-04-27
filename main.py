import random

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3

symbols_count = {
    "A": 1,
    "B": 1,
    "C": 3,
    "D": 8
}

symbols_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def get_winnings(lines,columns,bet):
    amount_won=0
    winning_lines=[]
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            if column[line] != symbol:
                break   
        else:
            amount_won += symbols_value[symbol]*bet*len(columns)
            winning_lines.append(line+1)  

    return amount_won,winning_lines


def get_slot_machine_spin(symbols,rows,cols):
    all_symbols = []
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []

    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:] #copy a list

        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i in range(len(columns)):
            if i != len(columns)-1:
                print(columns[i][row],end=" | ")
            else:
                print(columns[i][row],end="")
        print()


def deposit():
    while True:
        amount = input("What total amount would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount>0:
                break
            else:
                print("Enter amount greater than 0")
        else:
            print("Please enter a number")
    return amount


def get_number_of_lines(balance):
    while True:
        lines = input(f"Enter the number of lines you want for bet (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if lines > balance:
                print(f"Not enough balance for the entered lines, please give a line number within permissible balance limit.")
            elif 1<=lines<=MAX_LINES:
                break
            else:
                print(f"Enter a number between 1 and {MAX_LINES}")
        else:
            print("Please enter a valid number")
    return lines


def get_bet():
    while True:
        amount = input("What amount would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET<= amount <=MAX_BET:
                break
            else:
                print(f"Enter amount between ${MIN_BET}-${MAX_BET}")
        else:
            print("Please enter a number")
    return amount


def game(balance):
    lines = get_number_of_lines(balance)
    
    while True:
        bet = get_bet()
        total_bet = bet*lines

        if total_bet > balance:
            print(f"Your bet: ${total_bet} is more than deposited amount: ${balance}, kindly re-enter your betting amount.")
        else:
            break
        
    print(f"You are betting ${bet} on {lines} lines. Total bet = ${total_bet}")

    slots = get_slot_machine_spin(symbols_count,ROWS,COLS)
    print_slot_machine(slots)

    winning_amount,winning_lines = get_winnings(lines,slots,bet)

    print(f"You won on {len(winning_lines)} line(s):", *winning_lines)
    print(f"You have won amount = ${winning_amount}")

    net_winning = winning_amount-total_bet
    return net_winning

def main():
    balance = deposit()
    
    while True:
        spin = input("Press enter to spin (press 'q' to quit): ")
        if spin=="q":
            break

        net_winning = game(balance)
        balance += net_winning

        print(f"Your balance is: ${balance}")
        if balance < 1:
            break

    print(f"You left with ${balance}.")

main()