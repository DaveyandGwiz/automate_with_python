import re
from datetime import datetime

# Function to convert various date formats to a standard format (YYYY-MM-DD)
def standardize_date(date_str):
    # List of possible date formats
    date_formats = [
        '%m/%d/%Y',  # 3/14/2019
        '%m-%d-%Y',  # 03-14-2019
        '%Y/%m/%d',  # 2015/3/19
        '%Y-%m-%d',  # 2019-03-14
        '%Y.%m.%d',  # 2019.03.14
        '%d/%m/%Y',  # 14/03/2019 (for international formats)
        '%d-%m-%Y',  # 14-03-2019 (for international formats)
    ]

    for date_format in date_formats:
        try:
            # Attempt to parse the date string using the current format
            parsed_date = datetime.strptime(date_str, date_format)
            # Return the date in the standard format (YYYY-MM-DD)
            return parsed_date.strftime('%Y-%m-%d')
        except ValueError:
            # If parsing fails, try the next format
            continue
    # If no format matches, return the original date string
    return date_str

# Sample text containing dates in various formats
text = """
Here are some dates:
- 3/14/2019
- 03-14-2019
- 2015/3/19
- 2019-03-14
- 2019.03.14
- 14/03/2019
- 14-03-2019
"""

# Regular expression to find date-like patterns
date_pattern = re.compile(r'\b\d{1,4}[-/.]\d{1,2}[-/.]\d{1,4}\b')

# Replace dates in the text with the standardized format
cleaned_text = date_pattern.sub(lambda x: standardize_date(x.group()), text)

print("Original text:")
print(text)
print("\nCleaned text:")
print(cleaned_text)
