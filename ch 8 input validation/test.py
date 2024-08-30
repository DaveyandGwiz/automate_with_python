import pyinputplus as pyip

# Custom validation function
def handle_no_input(value):
    if value.lower() == 'no':
        return None  # Return None if the user inputs 'no'
    return value  # Otherwise, return the original value

# Using pyip.inputCustom() with the custom function
response = pyip.inputCustom(handle_no_input, prompt="Do you want to proceed? (yes/no): ")

# Output
if response is None:
    print("User chose not to proceed.")
else:
    print(f"User input: {response}")
