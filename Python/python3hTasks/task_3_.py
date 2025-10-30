import random
print("Think of a number between 1 and 100...")
# Keep track of the possible range
low = 1
high = 100
guesses = 0
while True:
    # Make a guess within the current valid range
    guess = random.randint(low, high)
    guesses += 1
    feedback = input(f"My guess is {guess}. (higher/lower/correct): ")
    if feedback.lower() == "correct":
        print(f"I got it in {guesses} guesses!")
        break
    elif feedback.lower() == "higher":
        # If your number is higher the new 'low' is one above the guess
        low = guess + 1
    elif feedback.lower() == "lower":
        # If your number is lower the new 'high' is one below the guess
        high = guess - 1
    else:
        print("Invalid input. Please enter 'higher', 'lower', or 'correct'.")
        guesses -= 1 # Don't count an invalid input as a guess
    # Optional add a check in case the user makes a mistake
    if low > high:
        print("Wait, you must have made a mistake! Let's restart.")
        # Reset the game
        low = 1
        high = 100
        guesses = 0