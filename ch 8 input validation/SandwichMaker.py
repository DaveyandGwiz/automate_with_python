import pyinputplus as pyip

breadCost = {'wheat':1,'white':2,'sourdough':3}
proteinCost = {'veggie':0,'beyond meat':3,'tofu':2}

def inputMenu(input):
    ingredients = ['bread','protein','mustard', 0]
    if input == 'no':
        print("Im being run")
        print (input)
        return ingredients
    ingredients = ['bread','protein','mustard', 0]
    print("what type of bread would you like? Wheat, white, or sourdough?")
    bread = pyip.inputStr(allowRegexes=[r'^(wheat|white|sourdough)$'])
    ingredients[0] = bread
    print("what type of protein would you like? Veggie, Beyond meat, or tofu?")
    protein = pyip.inputStr(allowRegexes=[r'^(veggie|beyond meat|tofu)$'])
    ingredients[1] = protein
    likeMustard = pyip.inputYesNo("Would you like mustard?")
    if likeMustard == 'yes':
        print("what type of mustard would you like? Yellow, brow, or spicy?")
        mustard = pyip.inputStr(allowRegexes=[r'^(yellow|brown|spicy)$'])
        ingredients[2] = mustard

    num_sandwiches = pyip.inputInt("How many sandwiches would you like? ")
    ingredients[3] = num_sandwiches

    return ingredients

print("would you like a sandwhich?")
response = pyip.inputCustom(inputMenu)
if response == ['bread','protein','mustard', 0]:
    print("have a noice day!")
    print("this is response %2", response)
else:
    print("You ordered a sandwhich made of %s", response)
    print("You\'re cost is %s" % ( response[3] * (breadCost[response[0]]+proteinCost[response[1]]) ))







