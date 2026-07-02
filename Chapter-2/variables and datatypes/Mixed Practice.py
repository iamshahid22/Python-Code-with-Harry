# Create variables:
# name
# age
# height
# weight
# is_married
# Print all values with their data types.
name = "Shahid"
age = 21
height = 172
weight = 58
is_married = False

print(name)
print(type(name))

print(age)
print(type(age))

print(height)
print(type(height))

print(weight)
print(type(weight))

print(is_married)
print(type(is_married))

# Given:
# x = "50"
# y = 20
# Convert x so you can add them and print the result.
x = "50"
y = 20
z = int(x)
sum = z+y
print(sum)

# Predict the output before running:
a = 10
b = "20"
print(str(a) + b)  # output: 1020

# Predict the datatype:
x = 5 / 2 
print(x)
print(type(x)) # float (quotient value displays) : 2.5

# Predict the datatype:
x = 5 // 2
print(x)
print(type(x)) # int () : 2

# Ask the user for:
# Name
# Age
# College

# Print:
# ----- Student Details -----
# Name    : Shahid
# Age     : 21
# College : AITS

Name = input("Enter your name:")
Age = int(input("enter ur age:"))
College = input("Enter your College name:")

print("----- Student Details -----")
print(f"Name: {Name}")
print(f"Age: {Age}")
print(f"College: {College}")

# Ask the user for two decimal numbers and print:
# Sum
# Difference
# Product
# Division
a = float(input("Enter a number:"))
b = float(input("Enter b number:"))
print("Sum:",a+b)
print("Diff:",a-b)
print("Div:",a/b)
print("Mul",a*b)

# Store the following values and identify their data types:
# 25
# 25.0
# "25"
# False
# 5+3j
a=25
b=25.0
c="25"
d=False
e=5+3j
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

# Ask the user to enter their birth year and calculate their approximate current age.
birth_year = int(input("Enter your Birth year:"))
current_year = 2026
age = current_year - birth_year
print("Your age is:", age)

