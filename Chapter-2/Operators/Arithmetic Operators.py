# Take two numbers as input and print:

# Sum
# Difference
# Product
# Quotient

num1 = int(input("Enter a number:"))
num2 = int(input("Enter a number:"))
print("Sum:", num1+num2)
print("Diff:", num1-num2)
print("Product:", num1*num2)
print("Quotient:", num1/num2)

# Find the remainder when 25 is divided by 4.
num = 25%4
print(num)

# Find the square of a number entered by the user.
num = int(input("Enter a number:"))
print(num**2)

# Find the cube of a number.
num = int(input("Enter a num:"))
print(num**3)

# Find the floor division (//) of two numbers.
num1 = int(input("Enter a num:"))
num2 = int(input("Enter b num:"))
print(num1//num2)

# Find the exponent (**) of two numbers.
a=int(input("enter num1:"))
b=int(input("enter num2:"))
print(a**b)

# Take three numbers and print their average.
a=9
b=44
c=7
avg = a+b+c/3
print("Average:",avg)

# Convert:
# 150 minutes into hours and remaining minutes.
hr = 60
mins = 150

hrs = mins//hr
print(f"{hrs}hrs {mins - hr*hrs}mins")

# Find whether a number is even or odd using %.
num = int(input("Enter number:"))
if num%2==0:
    print("Even!")
else:
    print("Odd!")
    
# Find the last digit of any number.
num = 143
last_digit = num%10
print(last_digit)

