import re


# Write a regular expression that can detect dates in the DD/MM/YYYY format.
# Assume that the days range from 01 to 31, the months range from 01 to 12,
# and the years range from 1000 to 2999.
# Note that if the day or month is a single digit, it’ll have a leading zero.
#
#
# The regular expression doesn’t have to detect correct days for each month
# or for leap years;
# it will accept nonexistent dates like 31/02/2020 or 31/04/2021.
# Then store these strings into variables named month, day, and year,
# and write additional code that can detect if it is a valid date.
# April, June, September, and November have 30 days, February has 28 days,
# and the rest of the months have 31 days.
# February has 29 days in leap years.
# Leap years are every year evenly divisible by 4,
# except for years evenly divisible by 100,
# unless the year is also evenly divisible by 400.
import re

def validFormat(date_string):
    # Define the regex pattern
    pattern = re.compile(r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/([12][0-9]{3})$')
    # Apply the regex pattern to each test string and print the results
    match = pattern.match(date_string)
    if match:
        print(f"'{date_string}' is a valid date")
        # Extract the day, month, and year from the match groups
        day, month, year = match.groups()
        return int(day), int(month), int(year)
    else:
        # If the date string is not valid, return None
        print(f"'{date_string}' is not a valid date")
        return None


def validDate(day, month, year):
    isLeapYear = False
    if year % 400 == 0:
        isLeapYear = True
    if not year % 100 == 0 and year % 4 == 0:
        isLeapYear = True

    # April, June, September, and November have 30 days, February has 28 days,
    # and the rest of the months have 31 days.
    # April 4, June 6, Sep 9, Nov 11
    if month in [4,6,9,11] and day == 31:
        print(f"'{day}-{month}-{year}' is not a real date")
        return
    #february has at most 28 days unless it is a leap year, then it can have at most 29 days
    if isLeapYear == True:
        if month == 2 and day > 29:
            print(f"'{day}-{month}-{year}' is not a real date")
            return
        else:
            print(f"'{day}-{month}-{year}' is a real date")
            return
    else:
        if month == 2 and day > 28:
            print(f"'{day}-{month}-{year}' is not a real date")
            return
        else:
            print(f"'{day}-{month}-{year}' is a real date")
            return


test_strings = [
    '29/02/2000',  # Valid date
    '31/12/2999',  # Valid date
    '15/05/1000',  # Valid date
    '00/01/2000',  # Invalid day
    '32/01/2000',  # Invalid day
    '15/13/2000',  # Invalid month
    '15/05/0999',  # Invalid year
    '5/5/2000',    # Invalid format
    '05/05/2000',  # Valid date
    '12/11/2020',  # Valid date
    '31/04/2020',  # Invalid day for month
]
for mydate in test_strings:
    if validFormat(mydate):
        day, month, year = validFormat(mydate)
        if day is not None:
            validDate(day, month, year)



