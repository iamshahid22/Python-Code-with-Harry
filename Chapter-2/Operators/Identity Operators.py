# Predict the output:
a = [1,2,3]
b = a
print(a is b) #True

# Predict:
a = [1,2,3]
b = [1,2,3]
print(a is b) #False

# Predict:
a = [1,2]
b = [1,2]
print(a == b) #True

# Explain the difference between == and is using your own example.
# == checks if the values are the same.
# is checks if the exact memory locations (identities) are the same.
# Create two separate lists with the exact same items
list_a = [1, 2, 3]
list_b = [1, 2, 3]

# Point a new variable directly to list_a
list_c = list_a

# --- Testing == (Value) ---
print(list_a == list_b)  # Returns True (They contain the same numbers)

# --- Testing is (Identity/Memory Location) ---
print(list_a is list_b)  # Returns False (They are stored in different places in memory)
print(list_a is list_c)  # Returns True (They point to the exact same object in memory)

# Create two variables that refer to the same list and check is and ==.
list1 = ["apple","banana","grapes"]
list2 = list1
print("list1 == list2:", list1==list2)
print("list1 is list2:", list1 is list2)