number = int(input("Enter a number: "))
is_prime = True
if number <= 1:
    is_prime = False
else:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break 
if is_prime:
    print(f"{number} is prime!")
else:
    print(f"{number} is not prime.")