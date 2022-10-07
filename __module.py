def main(choice):
    if choice == 1: # DEPOSIT
        try:
            amount = int(input("\nAmount to be Deposited: "))
        except:
            print("Invalid input!")
            main(choice)
        else:
            mode = "deposited"
            print("\nDeposit to Account Type")
            print("A. Savings")
            print("B. Current\n")
            
            account = input("Account Type: ").upper().strip()
            if account != 'A' and account != 'B':
                print("Option not found: [A / B]")
                main(choice)
            else:
                print()
                account = "savings" if account == 'A' else "current"
                perform_action(amount, account, mode)

    elif choice == 2: # WITHDRAW
        mode = "withdrawn"

        try:
            amount = int(input("\nAmount to be Withdrawn: "))
        except:
            print("Invalid input!")
            main(choice)
        else:
            print("\nAccount Type")
            print("A. Savings")
            print("B. Current\n")
            
            account = input("Account Type: ").upper().strip()
            if account != 'A' and account != 'B':
                print("Option not found: [A / B]\n")
                main(choice)
            else:
                print()
                account = "savings" if account == 'A' else "current"
                withdraw_isvalid(amount, account, mode)
                perform_action(amount, account, mode)

    elif choice == 3: # FUND TRANSFER
        mode = 'transferred'

        try:
            amount = int(input("\nAmount to be Transferred: "))
        except:
            print("Invalid input!")
            main(choice)
        else:
            print("\nTransfer From - To Account Type:")
            print("A. Savings to Current")
            print("B. Current to Savings\n")

            account = input("Account Type: ").upper().strip()
            if account != 'A' and account != 'B':
                print("Option not found: [A / B]\n")
                main(choice)
            else:
                print()
                account = "savings" if account == 'A' else "current"
                withdraw_isvalid(amount, account, mode)
                perform_action(amount, account, mode)
    
    elif choice == 4: # BALANCE INQUIRY
        print(f"\nSavings Balance: {user_balance['savings']}")
        print(f"Current Balance: {user_balance['current']}\n")
        run_again()

    else:
        print("Thank you for banking with us. Please remove your card...")



def perform_action(amt, acc, mode):

    if mode == 'deposited':
        user_balance[acc] += amt

    elif mode == "withdrawn":
        user_balance[acc] -= amt
    
    elif mode == 'transferred':

        tran_from = acc
        receiver = "current" if acc == 'savings' else "savings"
        user_balance[acc] -= amt
        user_balance[receiver] += amt
        
        acc = receiver
        

    print(f"Amount of {amt} is {mode} {'from' if mode == 'withdrawn' else 'to'} {acc.capitalize()} Account.")
    
    if mode == 'transferred':
        print(f"{tran_from.capitalize()} Balance: {user_balance[tran_from]}")

    print(f"{acc.capitalize()} Balance: {user_balance[acc]}\n")
    run_again()


def choose_tran():
    print("\nChoose a Transaction:")
    for i in range(len(transactions)):
        print(f"{i + 1} - {transactions[i]}")
    print()

def input_choice():
    while True:
        try:
            choice = int(input("Your Choice: "))
            if choice > 5 or choice < 1:
                raise Exception
        except:
            print("Invalid choice!\n")
        else:
            return choice

def withdraw_isvalid(amt, acc, mode):
    mode = 'transfer' if mode == 'transferred' else 'withdraw'
    if amt < 200:
        print(f"Cannot {mode} amount of less than 200.")
        choose_tran()
        main(input_choice())
            
    elif amt % 100 != 0:
        print(f"{mode.capitalize()} amount must be in multiple of 100.")
        print("(Ex. [200, 500, 1000, 2000, etc...])")
        choose_tran()
        main(input_choice())

    elif amt > user_balance[acc]:
        print(f"Error: cannot {mode} more than remaining balance")
        print(f"{acc.capitalize()} balance: {user_balance[acc]}")
        print(f"{mode.capitalize()} amount attempted: {amt}")
        choose_tran()
        main(input_choice())
    

def run_again():
    run = input("Do you want to do another Transaction? [y/n]: ").lower().strip()
    
    if run == 'y':
        choose_tran()
        main(input_choice())
    elif run == 'n':
        print("Thank you for banking with us. Please remove your card...")
        exit()
    else:
        print("Option not found!\n")
        run_again()


user_balance = {
    "savings": 0,
    "current": 0
}

transactions = ["Deposit", "Withdraw", "Fund Transfer", "Balance Inquiry", "Exit"]