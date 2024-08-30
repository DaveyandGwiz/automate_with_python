#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import re

emailRegex = re.compile(r'''
    ^[a-zA-Z0-9_.+-]+         # username: allow letters, numbers, underscores, dots, plus signs, and hyphens
    @                         # @ symbol
    [a-zA-Z0-9-]+             # domain name: allow letters, numbers, and hyphens
    (\.[a-zA-Z0-9-]+)*        # optional subdomains
    \.[a-zA-Z]{2,3}$           # top-level domain: allow letters only, and at least 2 characters long
''', re.VERBOSE)

# Test strings
test_strings = [
    "hello@world.com",
    "example.email@sub.domain.com",
    "just some text!",
    "@@@",
    "no special symbols",
    "daveandgwiz@gmail.com",
    "user+name@domain.co.uk",
    "user_name@domain.org",
    "user-name@domain.gov",
    "user.name@domain.edu",
    "user@domain.museum",
    "daveyandgwiz@gmail.com"
]

# Apply the regex pattern to each test string
for test_string in test_strings:
    matches = emailRegex.findall(test_string)
    if matches:
        print(f"Original: {test_string}")
        print(f"Filtered: {''.join(matches)}")
        print()
    else:
        print(f"Original: {test_string} does not match")
# TODO: Find matches in clipboard text.

# TODO: Copy results to the clipboard.