# Ask the user for their name and age. Print:
# Hello Shahid, you are 21 years old.
name = input("Enter your name:")
age = int(input("Enter your age:"))
print(f"Hello {name}, you are {age} years old.")

# Print your height with two decimal places.
height = 172.223
print(f"{height:.2f}")

# Print a bill using formatted strings.
item1 = "Mouse"
price1 = 999.9
item2 = "Notebook"
price2 = 50
total = price1 + price2
print(f"{item1}: {price1}Rs")
print(f"{item2}: {price2}Rs")

# Display student information neatly using formatting.
name = "Shahiddin Shaik"
rollno = "5c8"
branch = "CSE"
clg_name = "AITS"
cgpa = 6.87
print(f"Name: {name}")
print(f"Roll No: {rollno}")
print(f"Branch: {branch}")
print(f"College Name: {clg_name}")
print(f"Cgpa: {cgpa}")

# Create a receipt showing:
# Item
# Price
# Quantity
# Total
item = "Iphone 17 pro"
price = 170000
quantity = 2
total  = price * quantity
print("====Receipt====")
print(f"Item:      {item}")
print(f"Price:     {price} rs")
print(f"Quantity:  {quantity}")
print(f"Total:     {total} rs")

# Print your marks in aligned columns.
maths = 93
science = 90
hindi = 95
print(f"{'Subjects':<12}{'Marks':>5}")
print("_" * 18)

print(f"{'Maths':<12}{maths:>5}")
print(f"{'Science':<12}{science:>5}")
print(f"{'Hindi':<12}{hindi:>5}")

# Ask the user for three subjects and marks, then print a formatted report.
sub1 = input("Enter first subject name: ")
marks1 = int(input(f"Enter marks for {sub1}: "))

sub2 = input("Enter second subject name: ")
marks2 = int(input(f"Enter marks for {sub2}: "))

sub3 = input("Enter third subject name: ")
marks3 = int(input(f"Enter marks for {sub3}: "))
print("\n" + "=" * 22)
print(f"{'Subject':<15}{'Marks':>7}")
print("-" * 22)
print(f"{sub1:<15}{marks1:>7}")
print(f"{sub2:<15}{marks2:>7}")
print(f"{sub3:<15}{marks3:>7}")
print("=" * 22)

# Print your details using an f-string.
name = "Gemini"
creator = "Google"
type_of_ai = "Large Language Model"
release_year = 2026

print(f"=== AI ASSISTANT PROFILE ===")
print(f"Name:         {name}")
print(f"Creator:      {creator}")
print(f"Type:         {type_of_ai}")
print(f"Current Year: {release_year}")
print(f"============================")

# Print your details using .format().
name = "Gemini"
creator = "Google"
type_of_ai = "Large Language Model"
release_year = 2026

print("=== AI ASSISTANT PROFILE ===")
print("Name:         {}".format(name))
print("Creator:      {}".format(creator))
print("Type:         {}".format(type_of_ai))
print("Current Year: {}".format(release_year))
print("============================")

# Compare % formatting and f-strings by printing the same output both ways.
name = "Gemini"
version = 2.5
id_number = 7
print("AI: %s | Ver: %.1f | ID: %03d" % (name, version, id_number))
print(f"AI: {name} | Ver: {version:.1f} | ID: {id_number:03d}")