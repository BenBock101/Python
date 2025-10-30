total = 0  #track the sum of all numbers
count = 0  #track how many numbers were entered
while True:
    num = int(input("Enter a number (-1 to finish): "))
    if num == -1:
        # This is the stop signal
        break  # Exit the loop
    # These lines only run if num is NOT -1
    total += num  # Add the number to the running total
    count += 1    # Increment the count of valid numbers
# Check if any numbers were entered before dividing
if count == 0:
    print("No numbers were entered to calculate an average.")
else:
    # Calculate and print the average
    average = total / count
    print(f"Average: {average}")