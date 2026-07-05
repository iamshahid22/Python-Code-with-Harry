# Take the user's name and print it.
name = input("Enter ur name:")
print("Your name:",name)

# Take the user's age and print its type.
age= int(input("Enter ur age:"))
print("Your age:", age)

# Take two numbers as input and print their types.
num1 = int(input("Enter a number:"))
num2= float(input("Enter a number:"))
print(type(num1))
print(type(num2))

# Predict:
age = input("Enter age: ")
print(type(age)) # output : string 

# Take a decimal number as input and print its type.
num = float(input("Enter a number:"))
print(type(num))

# Take your college name as input and print it.
college_name = input("Enter ur college name:")
print(college_name)

# Take your city and state and print:
city = input("Enter your city name:")
state = input("enter ur state name:")
print(city)
print(state)

# Ask the user for two numbers and concatenate them without converting them.
num1 = input("Enter a number:")
num2 = input("Enter b number:")
print(num1 + num2)

# Ask the user for two numbers and add them correctly.
a = int(input("Enter a num:"))
b = int(input("Enter b num:"))
print(a+b)

# Explain why input() always returns a string.
# Because the input() function is designed to read user input as text, it returns the input as a string by default. 
# This allows for flexibility in handling different types of data, as the user can enter any characters, including letters, numbers, and symbols. 
# If you need to work with other data types, you can convert the string to the desired type (e.g., int, float) using appropriate type conversion functions.
