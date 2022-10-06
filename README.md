# ATM - SIMULATION

Python class program
Mid-term assignment

# SAMPLE RUN:

ATM SIMULATION - Banko De Uno

Enter Pin: 1234

Incorrect Pin!

Enter Pin: 123456

Choose a Transaction:
1-Deposit
2-Withdraw
3-Fund Transfer
4-Balance Inquiry
5-Exit

Your Choice: 1

Amount to be Deposited: 5000

Deposit to Account Type:
A. Savings
B. Current

Account Type: A

Amount of 5000 has been deposited to Savings.

Savings Balance: 5000

Do you want to do another Transaction? [y/n]: y

Choose a Transaction:
1-Deposit
2-Withdraw
3-Fund Transfer
4-Balance Inquiry
5-Exit

Your Choice: 2

Amount to be withdrawn: 2000

Withdraw from Account Type:
A. Savings
B. Current

Account Type: A

Amount of 2000 is withdrawn from Savings.

Savings Balance: 3000

Do you want to do another Transaction? [y/n]: y

Choose a Transaction:
1-Deposit
2-Withdraw
3-Fund Transfer
4-Balance Inquiry
5-Exit

Your Choice: 3

Amount to be transferred: 2000

Transfered From - To Account Type:
A. Savings to Current
B. Current to Savings

Account type: A

Amount of 2000 is transferred to Current Account.

Savings Balance: 1000
Current Balance: 2000

Do you want to do another Transaction? [y/n]: y

Choose a Transaction:
1-Deposit
2-Withdraw
3-Fund Transfer
4-Balance Inquiry
5-Exit

Your Choice: 4

Balance Inquiry
Savings: 1000
Current: 2000

Do you want to do another Transaction? [y/n]: y

Choose a Transaction:
1-Deposit
2-Withdraw
3-Fund Transfer
4-Balance Inquiry
5-Exit

Your Choice: 5

Thank you for banking with us. Please remove your card.

# Error Trapping Requirements:

1. Pin must be consists of numbers only and must be of length 6.
2. If incorrect pin is encoded for over 3 times then prompt user that card is confiscated.
3. The user cannot perform withdraw if the amount to be withdrawn is more than the amount in savings / current. Prompt the user of appropriate feedback.
4. The amount to be withdrawn must be a multiple of 100 and not less than 200.
5. Trap all other errors concerning invalid / incorrect inputs.

# Implementation Requirements:

1. Loop
2. Function
3. if...elif..else
4. string formatting
5. Try, Except, Else, Finally
6. All monetary values must be of int type
