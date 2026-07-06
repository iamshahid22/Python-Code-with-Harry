# Print the first character of "Python".
a = "Python"
print(a[0])

# Print the last character using positive indexing.
print(a[5])

# Print the last character using negative indexing.
print(a[-1])

# Print the third character of your name.
name = "Shahid"
print(name[2])

# Ask the user for their name and print its first letter.
name = input("Enter your name:")
print(name[0])

# Print the second-last character.
print(name[-2])

# Print every character one by one using indexing (without loops).
name = "Shahiddin"
for i in range(len(name)):
    print(i, name[i])
    
# What happens if you access an index that doesn't exist?
a = "Python"
print(a[10])  # This will raise an IndexError

# Predict the output:
# word = "Python"
# print(word[2])
# print(word[-3])
word = "Python"
print(word)
print(word[2])
print(word[-3])
