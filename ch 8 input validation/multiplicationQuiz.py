import pyinputplus as pyip
import random, time

numberOfQuestions = 10
correctAnswers = 0
for questionNumber in range(numberOfQuestions):
    # Pick two random numbers:
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)
    print(prompt)
    print("what is the solution?")
    response = pyip.inputStr()
    response = int(response)
    if response == num1 * num2:
        print("you\'re right!")
        correctAnswers += 1
    else:
        print("Almost, %s x %s = %s" % (num1,num2,(num1*num2)))

        