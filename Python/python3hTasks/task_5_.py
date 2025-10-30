import random
wins = 0
losses = 0
# Generate the very first number to start the game
current_num = random.randint(1, 100)
while True:
    print(f"\nCurrent number: {current_num}")
    guess = input("Will the next number be (h)igher or (l)ower? (q to quit): ")
    if guess.lower() == 'q':
        break  # Exit the loop if the user types 'q'
    # Validate input
    if guess.lower() not in ('h', 'l'):
        print("Invalid input. Please enter 'h', 'l', or 'q'.")
        continue # Skip the rest of this loop and start over
    # Generate the next number
    next_num = random.randint(1, 100)
    print(f"Next number: {next_num}")
    # Determine the correct answer
    if next_num > current_num:
        correct_answer = 'h'
    elif next_num < current_num:
        correct_answer = 'l'
    else:
        # Handles ties
        print("It's a tie! No score change.")
        current_num = next_num # The number still carries over
        continue # Skip win/loss check
    # Check the user's guess against the correct answer
    if guess.lower() == correct_answer:
        print("You win!")
        wins += 1
    else:
        print("You lose!")
        losses += 1
    # The "next" number becomes the "current" number for the next round
    current_num = next_num
    print(f"Score: {wins} wins, {losses} losses")
# This code runs after the loop is broken user typed 'q'
print("\nThanks for playing!")
print(f"Final Score: {wins} wins, {losses} losses")