word = input("Enter a word: ")
reversed_str = ""
for char in word:
    reversed_str = char + reversed_str
print(reversed_str)