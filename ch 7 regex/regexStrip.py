import re

# Write a function that takes a string and does the same thing as the strip() string method.
# If no other arguments are passed other than the string to strip,
# then whitespace characters will be removed from the beginning and end of the string.
# Otherwise, the characters specified in the second argument to the function will be removed from the string.

BeginPattern = r'^\s'  # Pattern to match one or more digits
endPattern = r'\s$'

repl = '#'        # Replacement string
string = "There are 123 apples and 456 oranges."

def stripChars(txt, chars=None):
    result = None
    if chars == None:
        result = re.sub(r'^\s+', '', txt)
        result = re.sub(r'\s$', '', result)
        return result
    else:
        # Escape any special characters in chars
        #chars = re.escape(chars)
        # Build a regex pattern to match any of the specified characters
        pattern = f'[{chars}]'
        print(pattern)
        result = re.sub(pattern, '', txt)
        return result

print(   stripChars(' My name is Dave. ', 'MDa' ) )
