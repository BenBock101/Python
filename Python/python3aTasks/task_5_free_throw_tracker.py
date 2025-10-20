# Ask user for the total number of attempts
attempts = int(input("How many free throws will you attempt? "))
# Start the score too zero before the loop starts
score = 0
# Loop for each attempt
# Range(1, attempts + 1) to get shot numbers like 1, 2, 3
for i in range(1, attempts + 1):
    # Ask the user if the shot was made or missed for the current attempt
    shot = input(f"Shot {i} (y/n): ")
    # Check the user's input.
    # .lower() makes the input to lowercase so 'Y' is also accepted
    if shot.lower() == 'y':
        # If the shot was made add 1 to the score
        score += 1
    # Print the score after each attempt
    print(f"Current score: {score}")
# After the loop is finished print the final result
print(f"Final score: {score} out of {attempts}")