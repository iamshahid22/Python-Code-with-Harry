# Convert "100" into an integer.
a = "100"
print(int(a))

# Convert "999" into an integer and multiply it by 2.
a = "999"
b = int(a)
print(b*2)

# Convert the input age into an integer and add 5.
age = input("Enter ur age:")
a = int(age)
print(a + 5)

# Predict:
print(int("50"))  # output: 50
print(type(int("50"))) #output: int
print(int("Hello")) # output: Gives ValueError
print(int("10.5")) # output : gives value error

# Take two numbers as strings and convert both into integers before adding.
num1 = input("Enter a num:")
num2 = input("enter a num:")
a = int(num1)
b = int(num2)
print("Adding :", a+b)

# Ask the user for a birth year and calculate age.
c_year = 2026
b_year = int(input("Enter your birth year:"))
c_age = c_year - b_year
print("Your age is now:", c_age) 

# Ask the user for a number and print its square after converting it.
a = int(input("enter a number:"))
print(a**2)

