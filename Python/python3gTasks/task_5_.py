import random
# Pick a number between 1 and 50
secret = random.randint(1, 50)
guesses = 0  # Initialize guess counter
print("I'm thinking of a number between 1 and 50...")
while True:
    # Get the user's guess
    guess = int(input("Your guess: "))
    # Increment the guess counter
    guesses += 1
    # Check the guess
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        # The guess is correct
        print(f"Correct! You got it in {guesses} guesses!")
        break  # Exit the loop