import random
import string

print("Welcome to Password Generator!")

# Ask user for password length
length = int(input("Enter password length: "))

# Combine letters, digits, and symbols
characters = string.ascii_letters + string.digits + string.punctuation

# Generate random password
password = ""

for i in range(length):
    password += random.choice(characters)

print("Generated Password:", password)