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
print(age)
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