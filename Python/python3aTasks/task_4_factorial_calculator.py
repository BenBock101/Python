# Ask the user for a number and convert it to an integer
number = int(input("Enter a number: "))
# Initialize the starting product for the calculation
# The factorial of 0 is 1, so this is the starting point
product = 1
# Loop through all numbers from 1 up to/including the user's number
# range(1, number + 1) generates the sequence 1, 2, 3, numbers
for i in range(1, number + 1):
    # Multiply the current product by the current number 'i'
    product = product * i
# Print the final calculated factorial using an f-string for formatting
print(f"The factorial of {number} is {product}")