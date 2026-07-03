# Check whether "a" is in "Shahid".
word = "Shahid"
needed = "a"
if needed in word:
    print("a letter is in Shahid")
else:
    print("not in shahid")
    
# Check whether 10 is in:
# numbers = [5,10,15,20]
numbers = [5,10,15,20]
num = 10
if num in numbers:
    print("10 in numbers")
else:
    print("not in numbers")
    
# Check whether "python" is in a sentence entered by the user.
sentence = input("Enter a sentence:")
word = "python"
if word in sentence:
    print("python is in sentence")
else:
    print("not in sentence")
    
# Check whether a character entered by the user exists in their name.
name = input("enter name:")
character = input("enter character:")
if character in name:
    print("character present in name")
else:
    print("character not in name")
    
# Predict:
print(5 in [1,2,3,4,5]) #true
print(8 not in [1,2,3]) #true

