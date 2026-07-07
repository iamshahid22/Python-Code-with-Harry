# Password Strength Checker
# At least 8 characters
# Contains uppercase
# Contains lowercase
# Contains a digit
password = "Shahiddin@22"

length_ok = len(password)>=8
has_upper = False
has_lower = False
has_digit = False

for char in password:
    if char.isupper():
        has_upper=True
    elif char.islower():
        has_lower=True
    elif char.isdigit():
        has_digit=True

if length_ok and has_upper and has_lower and has_digit:
    print("Strong password")
else:
    print("Weak Password")

# Email Validator
# Must contain @
# Must contain .
# No spaces
email = "shahiddinshaik1@gmail.com"

has_at = "@" in email
has_dot = "." in email
has_space = " " in email

if has_at and has_dot and not has_space:
    print("valid email")
else:
    print("invalid email")

# Username Validator
# Minimum 5 characters
# Only letters and numbers
# No spaces
username = "Shahid22"
length_ok = len(username)>=5
chars_ok = username.isalnum()

if length_ok and chars_ok:
    print("Valid username")
else:
    print("Invalid username")

# Word Counter
# Count words
# Characters
# Vowels
# Digits
# Spaces
text = "Python 3 is amazing!"

words_list = text.split()
word_count = len(words_list)

char_count = len(text)
vowel_count = 0
digit_count = 0
space_count = 0

vowels = "aeiouAEIOU"

for char in text:
    if char in vowels:
        vowel_count += 1
    if char.isdigit():
        digit_count += 1
    if char == " ":
        space_count += 1

print("Total Words:", word_count)
print("Total Characters (including spaces):", char_count)
print("Total Vowels:", vowel_count)
print("Total Digits:", digit_count)
print("Total Spaces:", space_count)

# Student Report Formatter
# Name
# Roll Number
# Department
# CGPA
# Print a clean report.
name = "Rahul Sharma"
roll_number = "2026CS104"
department = "Computer Science"
cgpa = 8.75
print("==============================")
print("       STUDENT REPORT         ")
print("==============================")

print(f"Name:          {name}")
print(f"Roll Number:   {roll_number}")
print(f"Department:    {department}")
print(f"CGPA:          {cgpa}")

print("==============================")

# Text Analyzer
# Given a paragraph, print:
# Total characters
# Total words
# Total lines
# Uppercase count
# Lowercase count
# Digit count
# Space count
paragraph = """Python is fun.
Learning it in 2026.
Code every day!"""

char_count = len(paragraph)
word_count = len(paragraph.split())
line_count = len(paragraph.splitlines())

upper_count = 0
lower_count = 0
digit_count = 0
space_count = 0

frequencies = {}

for char in paragraph:
    # Update type counts
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1
    elif char.isdigit():
        digit_count += 1
    elif char == " ":
        space_count += 1

    if char != "\n":
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1

most_frequent_char = max(frequencies, key=frequencies.get)

print("==============================")
print("        TEXT ANALYSIS         ")
print("==============================")
print(f"Total Characters : {char_count}")
print(f"Total Words      : {word_count}")
print(f"Total Lines      : {line_count}")
print(f"Uppercase Letters: {upper_count}")
print(f"Lowercase Letters: {lower_count}")
print(f"Digits           : {digit_count}")
print(f"Spaces           : {space_count}")
print(f"Most Frequent    : '{most_frequent_char}' (appears {frequencies[most_frequent_char]} times)")
print("==============================")