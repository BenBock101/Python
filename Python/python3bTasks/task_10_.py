count = int(input("How many Fibonacci numbers? "))
a = 0  
b = 1  
for _ in range(count):
    print(a, end=" ")
    next_num = a + b
    a = b
    b = next_num
print()