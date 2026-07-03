# Take age and check whether a person can vote and has an Aadhaar card.
age = int(input("Enter age:"))
has_aadhar = input("Do you have Aadhar card? (yes/no): ")

if age >= 18:
    print("You are eligible to vote")
else:
    print("Not eligible")
    
if has_aadhar == "yes":
    print("You have an Aadhar card")
else:
    print("You dont have Aadhar card")
    

# Check whether a student passed if marks are greater than or equal to 35 and attendance is at least 75%.
marks = float(input("Enter marks:"))
attandance = float(input("Enter attandance percentage:"))

if marks>= 35 and attandance>=75:
    print("Result: Passed")
else:
    print("Result: Failed")
    
# Check whether a person gets a discount if they are a student or a senior citizen.
person = input("Enter who you are (student/sr citizen/other):")

if person == "student" or person == "sr citizen":
    print("You get discount")
else:
    print("not eligible")
    

# Predict:
print(True and False) # false
print(True or False) #true
print(not True) #false

# Check whether a number lies between 10 and 100.
a = int(input("Enter number:"))
if a in range(10,100):
    print("In Range")
else:
    print("out of range")
    
    