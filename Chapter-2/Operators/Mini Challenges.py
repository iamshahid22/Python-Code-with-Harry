# Build a simple calculator using operators (+, -, *, /, %, //, **).
a = int(input("Enter a number:"))
operator = input("Enter operators (+, -, *, /, %, //, **):")
b = int(input("Enter b number:"))
if operator == "+":
    print("Addition:", a+b)
elif operator == "-":
    print("Substraction:", a-b)
elif operator=="*":
    print("Multiply:", a*b)
elif operator=="/":
    print("Division:", a/b)
elif operator == "%":
    print("Modulo:", a%b)
elif  operator == "//":
    print("Floor division:", a//b)
elif operator == "**":
    print("Exponential:", a**b)
else:
    print("Invalid !")
    
# Ask the user for a number and determine whether it is:
# Positive
# Negative
# Zero
num = int(input("Enter a number:"))
if num >= 1:
    print("Positive")
elif num <= -1:
    print("Negative")
else: 
    print("Zero")
    

# Swap two numbers without using a third variable.
a = 3
b = a
print(b)

# Ask the user for marks in five subjects and calculate:
# Total
# Average
# Percentage
sub1 = int(input("Enter marks:"))
sub2 = int(input("Enter marks:"))
sub3 = int(input("Enter marks:"))
sub4 = int(input("Enter marks:"))
sub5 = int(input("Enter marks:"))
total = sub1+sub2+sub3+sub4+sub5
average = total/5
percentage = (total/500)*100
print(total)
print(average)
print(percentage)

# Ask the user for two numbers and print all comparison results (==, !=, >, <, >=, <=).
a = int(input("enter number:"))
b = int(input("enter number:"))
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)
print(a>b)
print(a<b)

# Check if a year entered by the user is a leap year using operators.
year = int(input("Enter year:"))
if year%400 ==0 or (year%4==0 and year%100!=0):
    print("Leap year")
else:
    print("not leap year")
    
# Check if a number is divisible by both 3 and 5.
num = int(input("Enter a number:"))
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by 3 and 5")
else:
    print("not divisible by both")
    
# Find the largest of two numbers using comparison operators.
num1 = 23
num2 = 21
if num1>num2:
    print("Num1 is greater")
else:
    print("num2 is greater")
    
# Check whether a character entered by the user is a vowel using logical operators.
char = input("Enter a single letter:").lower()
if char == 'aeiou':
    print(f"'{char}' is a vowel")
else:
    print(f"'{char}' is a constant")
    

# Create a simple login check:
# Username = "admin"
# Password = "python123"
# Print "Login Successful" if both match, otherwise "Invalid Credentials"
username = "shahid"
password = "shahid@143"
if username == "shahid" and password == "shahid@143":
    print("Login Successfull !")
else:
    print("Invalid credentials")