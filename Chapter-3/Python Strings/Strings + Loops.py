# Print each character using a for loop.
text = "Shahiddin"
for i in text:
    print(i)
    
# Count vowels in a string.
word = "python programming"
vowels = "aeiou" or "AEIOU"
count = 0
for vowel in word:
    if vowel in vowels:
        count += 1
print(f"Vowels: {count}")

# Count consonants.
text = "Hello World"
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char.isalpha() and char not in vowels:
        count += 1

print(f"Consonants: {count}")

# Count spaces.
text = "Hello World From Python"
count = 0

for char in text:
    if char == " ":
        count += 1

print(f"Spaces: {count}")

# Count digits.
text = "Python 3.11 released in 2022"
count = 0

for char in text:
    if char.isdigit():
        count += 1

print(f"Digits: {count}")

# Count uppercase letters.
text = "Hello World"
count = 0

for char in text:
    if char.isupper():
        count += 1

print(f"Uppercase: {count}")

# Count lowercase letters.
text = "Hello World"
count = 0

for char in text:
    if char.islower():
        count += 1

print(f"Lowercase: {count}")

# Reverse a string without slicing (using a loop).
word = "python"
rev = ""
for i in word:
    rev = i + rev
print(rev)

# Print characters at even indexes.
text = "Computer"

for i in range(len(text)):
    if i % 2 == 0:
        print(f"Index {i}: {text[i]}")

# Print characters at odd indexes.
text = "Computer"

for i in range(len(text)):
    if i % 2 != 0:
        print(f"Index {i}: {text[i]}")
