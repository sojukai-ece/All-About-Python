"""
The Challenge: The Digital Wallet Tracker

At the very top of your script, set up your starting data by 
creating a variable named balance and setting it to the float value 50.00. 
Right below that, create an empty list named transactions that will act as 
a digital receipt to track the user's money movement.

Start an infinite while loop. Inside this loop, prompt the user to choose 
an action by asking them to type either deposit, withdraw, history, or quit, 
making sure to convert their answer to lowercase. If the user types quit, simply 
break the loop to end the program.

If the user types deposit, ask them how much money they want to add. Because the 
input() function always captures text as a string, you must wrap their input in 
the float() function so Python treats it as a math number. Add this number to their 
balance. Then, use .append() to add a formatted text string to the transactions list 
documenting the action (for example: "Deposited: $15.50"). Make sure to use the 
:.2f trick you learned earlier so the money always looks correct!

If the user types withdraw, ask them how much money they want to take out, and 
remember to convert their answer into a float. Before you let them take the money, use
an if statement to check if the amount they requested is strictly greater than their 
current balance. If it is, tell them they have insufficient funds. If they have enough 
money, subtract the amount from their balance and append a formatted string to the 
transactions list (for example: "Withdrew: $10.00").

If the user types history, check the length of the transactions list. 
If it is empty, tell them they have no transaction history yet. If it is not 
empty, print exactly --- Transaction History --- and use a for loop to print every 
receipt in the list. Finally, whether the list was empty or not, print their 
current total balance formatted to two decimal places. If the user types anything 
other than those four specific commands, print an invalid command message so the loop 
can start over.
"""

balance = 50.0

transactions = []

while True:
    action = input("Choose which action to perform deposit, withdraw, history, or quit: ").strip().lower()

    if action == "quit":
        print(f"Ending the transaction now.")
        break

    elif action == "deposit":
        add_depo = float(input("How much money do you want to add? "))
        balance += add_depo
        receipt = f"Deposited: ${add_depo:.2f}"
        transactions.append(receipt)
        print("Deposit successful")

    elif action == "withdraw":
        withdrawal = float(input("How much money you wnt to withdraw? "))

        if withdrawal > balance:
            print("Insufficient balance")
            break

        else:
            balance -= withdrawal
            receipt = f"Withdrawn amount: ${withdrawal:.2f}"
            transactions.append(receipt)
            print("Withdrawal successful")

    elif action == "history":
        if len(transactions) == 0:
            print("No trasactions yet")
        else:
            print(transactions)
            for record in transactions:
                print(record)
