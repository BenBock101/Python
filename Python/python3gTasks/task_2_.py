total_sum = 0
# Start an infinite loop that'll be controled with 'break'
while True:
    # Get user input and convert it to an integer
    num = int(input("Enter a number (0 to stop): "))
    # Check if the user entered the stop value
    if num == 0:
        break  # Exit the loop
    # If not 0, add the number to thecl total
    total_sum += num
print(f"Total sum: {total_sum}")