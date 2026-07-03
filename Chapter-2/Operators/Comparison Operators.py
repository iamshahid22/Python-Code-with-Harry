# Take two numbers and print:
# Greater than
# Less than
# Equal to
# Not equal to
num1 = int(input("Enter a number:"))
num2 = int(input("Enter a number:"))
print(f"Greater than: {num1>num2}")
print(f"Less than: {num1<num2}")
print(f"Equal to: {num1 == num2}")
print(f"Not equal to: {num1 != num2}")

# Check whether two numbers are equal.
a = int(input("Enter a number:"))
b = int(input("Enter b number:"))
if a == b:
    print("A and B are equal")
else:
    print("Not equal")
    
# Check whether one number is greater than another.
a = 21
b = 19
if a>b:
    print("a is greater")
else:
    print("b is greater")
    
# Predict:
print(5 > 2) #true
print(5 < 2) #false
print(5 == 5) #true
print(5 != 5) #false

# Check if a person is eligible to vote (age ≥ 18).
age = int(input("Enter age:"))
if age>=18:
    print("You are eligible to vote!")
else:
    print("Not eligible!")
    
