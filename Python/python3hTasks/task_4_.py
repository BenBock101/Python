import random
# A list to store our unique numbers
numbers = []
# Loop until we have 6 numbers in our list
while len(numbers) < 6:
    # Generate a random number from 1 to 49
    num = random.randint(1, 49)
    # Check if this number is already in our list
    if num not in numbers:
        # If it's not, add it
        numbers.append(num)
# Print the final list
print("Your lottery numbers:", end=" ")
for num in numbers:
    print(num, end=" ")
print()
#Mr.McMaster has a underground gambaling ring in class. + 100,000,000.00 $$$$$$$$ all in on black