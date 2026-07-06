# Concatenate your first and last name.
first_n = "Shahiddin"
last_n = "shaik"
concatinate = first_n + last_n
print(concatinate)

# Repeat "Hi" five times.
for i in range(5):
    print("Hi")
    
# Ask for first and last name and join them.
first_name = input("Enter your first name:")
last_name = input("Enter your last name:")
full_name = first_name + last_name
print(full_name)

# Check if "Python" is in a sentence.
sentence = """I love Python Programming, 
i love doing python coding!""" 
print(sentence.find("Python"))

# Check if "Java" is not in a sentence.
print(sentence.find("Java"))

# Predict:
print("Py" + "thon") #output: Python

# Predict:
print("Hi" * 4) #output: HiHiHiHi

# Concatenate three strings.
str1 = "abcd"
str2 = "efgh"
str3 = "ijkl"
concatinate = str1 + str2 + str3
print(concatinate)

# Create your full address using concatenation.
Hno = "1-23 "
street_name = "OC colony "
town_name = "Kodumur"
print(f"Hno: {Hno}, Street: {street_name}, town: {town_name}.")

# Print a separator line using "=" * 40.
print("=" * 40)