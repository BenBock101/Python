# Ask the user for their name and store it in the 'name' variable
name = input("Enter your name: ")
# Ask how many times to print it and convert the input string to an integer
times_to_print = int(input("How many times? "))
# Loop the specified number of times
for _ in range(times_to_print):
    # Print the name followed by a space instead of a newline
    print(name, end=" ")
# also print a newline character at the very end to move the cursor
# to the next line in the terminal for a cleaner finish
print()