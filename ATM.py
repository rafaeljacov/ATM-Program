from __module import perform_action
from __module import choose_tran
from __module import input_choice
from __module import withdraw_isvalid
from __module import run_again
from __module import main

print("ATM SIMULATION - Banko De UNO")

for v in range(3):
    if v == 3:
        print("Your card has been confiscated due to entering incorrect pin three times...")
        exit()

    try:
        pin = int(input('Enter PIN: '))
    except:
        v += 1
        print("Incorrect Pin!\n")
    else:
        if len(str(pin)) == 6:
            choose_tran()
            break
        else:
            v += 1
            print("Incorrect Pin!\n")


main(input_choice())