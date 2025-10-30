# Define the correct password
correct_password = "python123"
# Start an infinite loop
while True:
    # Ask the user for the password
    password = input("Enter password: ")
    # Check if the guess matches the correct password
    if password == correct_password:
        print("Access granted!")
        break  # Exit the loop on success
    else:
        # If it doesn't match, print an error and the loop continues
        print("Incorrect! Try again.")