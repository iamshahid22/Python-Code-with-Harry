# Print the first three letters of "Python".
# Print the last three letters.
a = "Python"
print(a[:3])
print(a[-1:-3])

# Print every alternate character.
text = "Python Programming"
print(text[::2])

# Reverse a string using slicing.
string = "Shahid"
print(string[::-1])

# Print characters from index 2 to 5.
a = "Programming"
print(a[2:5])

# Slice your own name into first half and second half.
name = "Shahid Shaik"
mid = len(name)//2
first_half = name[:mid]
second_half = name[mid:]
print("First half:", first_half)
print("Second half:", second_half)

# Predict:
word = "Programming"
print(word[3:8]) #output: gramm

# Predict:
word = "Python"
print(word[::-1]) #output: nohtyP

# Predict:
word = "Developer"
print(word[::2]) #output: Dvlpr

# Print all characters except the first one.
a = "Sshahid"
print(a[1:])