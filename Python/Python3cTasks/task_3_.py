text = input("Enter text: ") #checks vowels and consonants ingnoring other characters
vowels = 0
consonants = 0
vowel_list = "aeiou"
for char in text: #is character a letter
    if char.isalpha():
        char_lower = char.lower() 
        if char_lower in vowel_list:
            vowels += 1
        else:
            consonants += 1
print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")