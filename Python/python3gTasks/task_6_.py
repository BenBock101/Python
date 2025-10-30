# Start an infinite loop to keep asking until a valid input
while True:
    grade = int(input("Enter a grade (0-100): "))
    # Check for validity (inclusive)
    if grade >= 0 and grade <= 100:
        # If valid, print confirmation and exit the loop
        print(f"Valid grade accepted: {grade}")
        break
    else:
        # If invalid, print error and the loop repeats
        print("Invalid! Must be between 0 and 100.")