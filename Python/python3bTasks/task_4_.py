number = int(input("Enter a number: "))
total = 0
for i in range(1, number + 1):
    total += i  
print(f"The sum of numbers 1 to {number} is {total}")