import pyinputplus as pyip


def addsUpToTen(numbers):
    # add the numbers in numbers list
    numbersList = list(numbers) # create array of correct size but need to correct type
    for i, digit in enumerate(numbersList):
        numbersList[i] = int(digit)
    # print if sum of number == 10
    if sum (numbersList) != 10:
        print("numbers should add up to 10 not %s" % sum(numbersList))
    else:
        print("sum is 10!") # print if sum of number != 10

    return int(numbers) # Return an int form of numbers.

response = pyip.inputCustom(addsUpToTen) # No parentheses after
print(response)
