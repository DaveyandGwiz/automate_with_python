# Strong Password Detection
# Write a function that uses regular expressions to make sure the password string it is passed is strong.
# A strong password is defined as one that is at least eight characters long, contains both uppercase and lowercase characters,
# and has at least one digit.
# You may need to test the string against multiple regex patterns to validate its strength.
import re

def isPasswordStrong(password):
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    return True

# Test the function with some example passwords
passwords_to_test = [
    'Password123',      # Strong password
    'password123',      # Missing uppercase character
    'PASSWORD123',      # Missing lowercase character
    'Password',         # Missing digit
    'Pass123',          # Less than 8 characters
    'StrongPass1',      # Strong password
    '12345678',         # Missing uppercase and lowercase characters
    'abcdefgh',         # Missing uppercase characters and digits
    "aB1",
    "aA1!&@&**$(#"
]

for pwd in passwords_to_test:
    print(f"'{pwd}' is a strong password: {isPasswordStrong(pwd)}")

