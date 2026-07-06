# Convert your name to uppercase.
name = "shahid"
print(name.upper())

# Convert it to lowercase.
print(name.lower())

# Capitalize your name.
print(name.capitalize())
# Convert a sentence to title case.
sentence = "hello wolrd from python"
print(sentence.title())

# Swap uppercase to lowercase and vice versa.
Sentence = "Hi, my name is Shahiddin shaik"
print(Sentence.swapcase())

# Count how many times "a" appears in a word.
word = "Shahiddin Shaik"
print(word.count("a"))

# Find the position of "o" in "Programming".
a = "Programming"
print(a.find("o"))

# Replace "Python" with "Java" in a sentence.
sentence = "I like Python coding!"
print(sentence.replace("Python","Java"))

# Check if a string starts with "Py".
string = "Programming Python.py"
print(string.startswith("Py"))

# Check if a string ends with ".py".
print(string.endswith(".py"))

# Remove spaces from both ends of a string.
word = " Shahiddin Shaik "
print(word.strip())
# Remove only left spaces.
print(word.lstrip())
# Remove only right spaces.
print(word.rstrip())

# Split a sentence into words.
sentence = "Python is fun to learn"
words = sentence.split()
print(words)

# Join a list of words into one string.
words = ["Python", "is", "fun", "to","learn"]
sentence = " ".join(words)
print(sentence)

# Check whether a string contains only digits.
text = "12345"
print(text.isdigit())

# Check whether a string contains only alphabets.
text = "shahid22"
text2 = "shahid"
print(text.isalpha())
print(text2.isalpha())

# Check whether a string is alphanumeric.
a = "shahid22"
print(a.isalnum())

# Check whether all characters are lowercase.
word = "PyThon"
print(word.islower())

# Check whether all characters are uppercase.
a = "SHAHID"
print(a.isupper())