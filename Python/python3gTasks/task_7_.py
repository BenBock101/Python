number = int(input("Enter a number: "))
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    product = 1
    # Use a copy of the number for the calculation
    #print the original number at the end
    count = number 
    while count > 0:
        product *= count  # product = product * count
        count -= 1      # Decrement the counter
    # This also correctly handles 0!, as the loop will not run
    # and the product will remain 1.
    print(f"{number}! = {product}")