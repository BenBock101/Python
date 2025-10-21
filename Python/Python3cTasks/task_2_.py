text = input("Enter some text: ") #checks for amount of a's
count = 0 
for char in text:
    if char == 'a':
        count += 1 # adds if a is found
print(f"The letter 'a' appears {count} times")