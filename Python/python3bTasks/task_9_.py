count = int(input("How many numbers? "))
total = 0
for i in range(1, count + 1):
    number = float(input(f"Enter number {i}: "))
    total += number  
if count > 0:
    average = total / count
    print(f"The average is {average}")
else:
    print("Cannot calculate the average of 0 numbers.")