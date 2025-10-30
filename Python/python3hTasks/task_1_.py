import random
print("Rolling a die 10 times:")
# Loop 10 times
for _ in range(10):
    # Generate a random integer between 1 and 6 (inclusive)
    roll = random.randint(1, 6)
    # Print the roll, with a space at the end instead of a newline
    print(roll, end=" ")
print()