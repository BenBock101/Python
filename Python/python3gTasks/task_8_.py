# Is this not what me and yuaroslav did for team 7???
# Starting balance (using float for currency)
balance = 1000.00
print("Welcome to the ATM!")
# Main program loop
while True:
    # Print the menu options
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = input("Choice: ")
    if choice == "1":
        # Check Balance
        # Format the output to 2 decimal places for currency
        print(f"Your balance: ${balance:.2f}")
    elif choice == "2":
        # Deposit
        amount = float(input("Deposit amount: $"))
        if amount > 0:
            balance += amount
            print(f"New balance: ${balance:.2f}")
        else:
            print("Invalid amount. Deposit must be positive.")
    elif choice == "3":
        # Withdraw
        amount = float(input("Withdraw amount: $"))
        if amount <= 0:
            print("Invalid amount. Withdrawal must be positive.")
        elif amount > balance:
            # Check for sufficient funds
            print(f"Insufficient funds! Your balance is ${balance:.2f}.")
        else:
            # If all checks pass, complete the withdrawal
            balance -= amount
            print(f"Withdrawal successful. New balance: ${balance:.2f}")
    elif choice == "4":
        # Exit
        print("Thank you for using our ATM!")
        break  # This is the only way to exit the main loop
    else:
        # Handle invalid menu choices
        print("Invalid choice. Please select 1-4.")