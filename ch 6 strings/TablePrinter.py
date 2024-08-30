tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def largestStrLen(list):
    largestLength = 0
    for string in list:
        if len(string) > largestLength:
            largestLength = len(string)
    return largestLength

def printTable(tableData):
    NumOfColumns = len(tableData)
    NumOfRows = len(tableData[0])
    colwidth = [0] * len(tableData)
    for i in range(len(tableData)):
        colwidth[i] = largestStrLen(tableData[i])

    for i in range(NumOfRows):
        for j in range(NumOfColumns):
            print(tableData[j][i].rjust(colwidth[j]),end=" ")
        print()

myData = [
            ['prime',  'megatron', 'grimlock', 'starscream'],
             ['truck', 'gun',      'dino',      'jet'],
             ['1st',  '1st',       '1st',       '2nd']
        ]
printTable(myData)