# Ask the user for:
# Name
# Age
# Height
# Print all values with their data types.
Name = input("Enter your name:")
Age = int(input("Enter your age:"))
Height = float(input("Enter your height:"))
print(Name)
print(type(Name))
print(Age)
print(type(Age))
print(Height)
print(type(Height))


# Predict the output:
x = input("Enter:")
print(type(x)) #output : string 

# Predict:
print(int(float("20.9"))) #output: 20

# Predict:
print(str(int(50.8))) #output: '50'

# Predict:
print(float(int("25"))) #output: 25.0

# What error occurs?
int("10a") #output: value error

# What error occurs?
float("abc") #output: value error

# Write a program that takes three numbers as input and prints:
# Sum
# Average
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
sum = a+b+c
avg = a+b+c/3
print(sum)
print(avg)

# Ask the user for a price and quantity. Calculate the total bill.
price = float(input("Enter price:"))
quantity = int(input("Enter quantity:"))
total = price*quantity
print("Total bill:", total)

# Build a small "Student Information" program that asks for:
# Name
# Roll Number
# Age
# CGPA
# Then print each value along with its data type.
Name = input("Enter your name:")
rollnumber = input("Enter ur rollnumber:")
age = int(input("Enter ur age:"))
cgpa = float(input("Enter ur cgpa:"))
print(Name)
print(type(Name))
print(rollnumber)
print(type(rollnumber))
print(age)
print(type(age))
print(cgpa)
print(type(cgpa))


# Create a program that asks the user for:
# Name
Name = input("Enter your name:")
# Birth Year
b_year = int(input("Enter your Birth year:"))
c_year = 2026
# Height
Height = float(input("Enter your height:"))
# Weight
weight = float(input("Enter you weight:"))
# College Name
clg_name = input("Enter your clg name:")
# CGPA
cgpa = float(input("Enter your cgpa:"))
# Then:
# Convert values to the correct data types.

# Calculate approximate age.
age = c_year - b_year
# Print all details.
print(Name)
print(type(Name))
print(age)
print(type(age))
print(Height)
print(type(Height))
print(weight)
print(type(weight))
print(clg_name)
print(type(clg_name))
print(cgpa)
print(type(cgpa))
# Print the data type of every variable.
# Print a formatted summary at the end.

print(f"Student Information:")
print(f"Name: {Name} (Type: {type(Name)})")
print(f"Age: {age} (Type: {type(age)})")
print(f"Height: {Height} (Type: {type(Height)})")
print(f"Weight: {weight} (Type: {type(weight)})")
print(f"College Name: {clg_name} (Type: {type(clg_name)})")
print(f"CGPA: {cgpa} (Type: {type(cgpa)})")
