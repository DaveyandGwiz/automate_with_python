# Write a function named collatz() that has one parameter named number.
# If number is even, then collatz() should print number // 2 and return this value.
# If number is odd, then collatz() should print and return 3 * number + 1.
#
# Then write a program that lets the user type in an integer and that keeps calling collatz()
# on that number until the function returns the value 1.


def collatz(number):
    if number % 2 == 0:
        print (number // 2)
        return number // 2
    if (number % 2) != 0:
        print (3 * number + 1)
        return 3 * number + 1

while True:
    try:
        response = int(input('Gimmie a number: '))
        break
    except ValueError:
        print("Please enter a valid integer.")

number = response
while True:
    # this keeps taking coll of response
    # i need the function to take the repsoend of collatz and then run a funtion on that

    number  = collatz(number)

    if number == 1:
        break


