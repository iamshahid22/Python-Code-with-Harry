# Create a variable x = 20.

# Perform one by one:

# +=
# -=
# *=
# /=
# //=
# %=
# **=

# Print the value after each operation.
x = 20

x += 5
print("After +=:",x)

x -= 2
print("after -=:",x)

x *= 3
print("after *=:",x)

x /= 4
print("after /=:",x)

x //= 5
print("after //=:",x)

x %= 4
print("after %=:",x)

x **= 5
print("after **=:",x)


# Predict the output before running:
x = 10
x += 5
x *= 2
print(x) #output: 30

# Predict:
x = 50
x //= 4
print(x) #output:12

# Predict:
x = 9
x **= 2
print(x) #output:81

# Write a program that keeps adding numbers to a variable using +=.
total = 0
while True:
    user_input = input("Enter a number or 'stop':")
    
    if user_input == "stop":
        break
    
    total +=int(user_input)
    print("Current total:", total)
    
print("Final total:", total)


