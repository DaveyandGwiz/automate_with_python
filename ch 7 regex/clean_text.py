import re

def clean_text(text):
    # Remove multiple spaces between words
    text = re.sub(r'\s+', ' ', text)

    # Remove accidentally repeated words (e.g., "accidentally accidentally")
    #text = re.sub(r'\b(\w+)\s+\1\b', r'\1', text, flags=re.IGNORECASE)
    text = re.sub(r'\b(\w+)\s+\1\b', r'pokemon', text, flags=re.IGNORECASE)

    # Remove multiple exclamation marks at the end of sentences
    text = re.sub(r'!{2,}', '!', text)

    return text

# Sample text with common typos and sensitive information
sample_text = """
This this is is a a sample sample  text with some common typos. 
"""

# Clean the text
cleaned_text = clean_text(sample_text)

# Print the results
print("Original text:")
print(sample_text)
print("\nCleaned text:")
print(cleaned_text)
