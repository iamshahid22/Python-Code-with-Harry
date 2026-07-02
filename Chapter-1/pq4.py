import os

# View and change working directory
print(os.getcwd())       
os.chdir('/')

# List files in the new directory
print(os.listdir('.'))
