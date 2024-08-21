import string
import random

# Define character sets
s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

# Get user input
characters_numbers = input("How many characters for the password do you want? ")

while True:
    try:
        characters_numbers = int(characters_numbers)
        if characters_numbers < 6:
            print("Password should be at least 6 characters long.")
            characters_numbers = input("Please enter a number again: ")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a number only.")
        characters_numbers = input("How many characters for the password? ")

# Shuffle character sets
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

# Calculate parts
part1 = round(characters_numbers * 30 / 100)
part2 = round(characters_numbers * 20 / 100)
part3 = characters_numbers - part1 - part2  # Remaining characters

# Create password
password = []
password.extend(s1[:part1])
password.extend(s2[:part1])
password.extend(s3[:part2])
password.extend(s4[:part2])

# Ensure the password has the required length
if len(password) < characters_numbers:
    additional_characters = characters_numbers - len(password)
    all_characters = s1 + s2 + s3 + s4
    random.shuffle(all_characters)
    password.extend(all_characters[:additional_characters])

# Shuffle the final password and convert to string
random.shuffle(password)
password = "".join(password)

print("Generated Password:", password)
