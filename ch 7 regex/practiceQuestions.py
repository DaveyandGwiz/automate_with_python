import re
# Practice Questions
# 1. What is the function that creates Regex objects?
# The re.compile() function creates Regex objects.
# 2. Why are raw strings often used when creating Regex objects?
#Raw strings (prefixed with r) are used to avoid escaping backslashes.
# This makes the pattern more readable and easier to write, as backslashes are treated literally.
# 3. What does the search() method return?
#The search() method returns a Match object if the pattern is found in the string; otherwise, it returns None
# You can use the group() method of the Match object to get the actual strings that match the pattern.
# For example, match.group() returns the whole match, and match.group(n) returns the nth group.

# Define a regular expression pattern to search for a word

# Define a regular expression pattern with capturing groups
# 4. How do you get the actual strings that match the pattern from a Match object?

# pattern = re.compile(r'(\d{4})-(\d{2})-(\d{2})')
#
# # Example string
# text = "The date is 2023-08-03."
#
# # Use search() to find the pattern in the text
# match = pattern.search(text)
#
# # Check if the pattern was found
# if match:
#     print("Pattern found!")
#     print(f"Entire match: {match.group(0)}")  # Entire match
#     print(f"Year: {match.group(1)}")          # First capturing group
#     print(f"Month: {match.group(2)}")         # Second capturing group
#     print(f"Day: {match.group(3)}")           # Third capturing group
# else:
#     print("Pattern not found.")

#
# 5. In the regex created from r'(\d\d\d)-(\d\d\d-\d\d\d\d)', what does group 0 cover? Group 1? Group 2?
#Group 0 covers the entire match.
# Group 1 covers the first set of digits: (\d\d\d).
# Group 2 covers the second set of digits: (\d\d\d-\d\d\d\d).

# 6. Parentheses and periods have specific meanings in regular expression syntax.
# How would you specify that you want a regex to match actual parentheses and period characters?
# escape the with a backslack

# 7. The findall() method returns a list of strings or a list of tuples of strings.
# What makes it return one or the other?
# Pattern without capturing groups
# returns a list of strings if the regular expression pattern contains no capturing groups.
# If the pattern contains one or more capturing groups, findall() returns a list of tuples.
# Each tuple contains the matched strings for each capturing group.
# pattern = re.compile(r'\b\d{4}\b')
#
# # Example text
# text = "These years are important: 1990, 2000, and 2023."
#
# # Use findall() to find all matches
# matches = pattern.findall(text)
#
# print("Matches without capturing groups:")
# print(matches)
# # Pattern with capturing groups
# pattern = re.compile(r'(\d{4})-(\d{2})-(\d{2})')
#
# # Example text
# text = "Important dates: 2023-08-03 and 2020-05-14."
#
# # Use findall() to find all matches
# matches = pattern.findall(text)
#
# print("Matches with capturing groups:")
# print(matches)
# 8. What does the | character signify in regular expressions?
# Logical OR
# Define a pattern that matches either "cat" or "dog"
pattern = re.compile(r'cat|dog')

# Example text
text = "I have a cat and a dog."

# Use findall() to find all matches
matches = pattern.findall(text)

print("Matches:", matches)
# 9. What two things does the ? character signify in regular expressions?
#
# 10. What is the difference between the + and * characters in regular expressions?
#
# 11. What is the difference between {3} and {3,5} in regular expressions?
#
# 12. What do the \d, \w, and \s shorthand character classes signify in regular expressions?
#
# 13. What do the \D, \W, and \S shorthand character classes signify in regular expressions?
#
# 14. What is the difference between .* and .*??
#
# 15. What is the character class syntax to match all numbers and lowercase letters?
#
# 16. How do you make a regular expression case-insensitive?
#
# 17. What does the . character normally match? What does it match if re.DOTALL is passed as the second argument to re.compile()?
#
# 18. If numRegex = re.compile(r'\d+'), what will numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens') return?
# numRegex = re.compile(r'\d+')
# newString = numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens')
# print(newString) #X drummers, X pipers, five rings, X hens

# 19. What does passing re.VERBOSE as the second argument to re.compile() allow you to do?
#
# 20. How would you write a regex that matches a number with commas for every three digits?
# It must match the following:
#
# '42'
# '1,234'
# '6,368,745'
# but not the following:
#
# '12,34,567' (which has only two digits between the commas)
# '1234' (which lacks commas)
# Define the regex pattern
# pattern = re.compile(r'^\d{1,3}(,\d{3})*$')
#
# # Test strings
# test_strings = ['42', '1,234', '6,368,745', '12,34,567', '1234']
#
# # Apply the regex pattern to each test string and print the results
# for s in test_strings:
#     if pattern.match(s):
#         print(f"'{s}' is a match")
#     else:
#         print(f"'{s}' is not a match")
# 21. How would you write a regex that matches the full name of someone whose last name is Watanabe?
# You can assume that the first name that comes before it will always be one word that begins with a capital letter.
# The regex must match the following:
#
# 'Haruto Watanabe'
# 'Alice Watanabe'
# 'RoboCop Watanabe'
# but not the following:
#
# 'haruto Watanabe' (where the first name is not capitalized)
# 'Mr. Watanabe' (where the preceding word has a nonletter character)
# 'Watanabe' (which has no first name)
# 'Haruto watanabe' (where Watanabe is not capitalized
# pattern = re.compile(r'[A-Z][a-z]*\sWatanabe')
# mylist = ['Haruto Watanabe','Alice Watanabe','RoboCop Watanabe','haruto Watanabe']
# result = pattern.findall(mylist[len(mylist)-2])
# print(result)

# 22.
# How would you write a regex that matches a sentence where the first word is either Alice, Bob, or Carol;
# the second word is either eats, pets, or throws; the third word is apples, cats, or baseballs;
# and the sentence ends with a period? This regex should be case-insensitive. It must match the following:
#
# 'Alice eats apples.'
# 'Bob pets cats.'
# 'Carol throws baseballs.'
# 'Alice throws Apples.'
# 'BOB EATS CATS.'
# but not the following:
#
# 'RoboCop eats apples.'
# 'ALICE THROWS FOOTBALLS.'
# 'Carol eats 7 cats.'
pattern = re.compile(r'^(Alice|Bob|Carol)\s*(eats|pets|throws)\s*(apples|cats|baseballs)\.',re.IGNORECASE)
# Test strings
test_strings = [
    'Alice eats apples.',
    'Bob pets cats.',
    'Carol throws baseballs.',
    'Alice throws Apples.',
    'BOB EATS CATS.',
    'RoboCop eats apples.',
    'ALICE THROWS FOOTBALLS.',
    'Carol eats 7 cats.'
]
# Apply the regex pattern to each test string and print the results
for s in test_strings:
    if pattern.match(s):
        print(f"'{s}' is a match")
    else:
        print(f"'{s}' is not a match")
