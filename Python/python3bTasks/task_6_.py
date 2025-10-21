lower = int(input("Enter lower bound: "))
upper = int(input("Enter upper bound: "))
total = 0
for i in range(lower, upper + 1):
    total += i
print(f"The sum of numbers from {lower} to {upper} is {total}")