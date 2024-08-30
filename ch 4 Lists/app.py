import copy

a = [1,2,3]
b = copy.copy(a)
b = [4,5,6]
print(a)
print(b)


spam = [2, 4, 6, 8, 10]

spam[3] = '4th member'
print(spam)

#print(spam[int(int('3' * 2) // 11)])
#print(spam[:2])
tofu = [3.14, 'cat', 11, 'cat', True]

print(tofu.index('cat'))
print(tofu.append(99))
print(tofu)
tofu.insert(1,'second item')
# print(tofu)
#
# for letter in 'word':
#     print(letter)
#
# mytuple = (1,2)
# print(mytuple[1])
#
# my_list = [1,2,3]
# another_list = my_list
# my_list = [4,5,6]
# print(another_list)


spam = ['apples', 'bananas', 'tofu', 'cats']

def printList(inputList):
    if inputList == []:
        return "empty list"
    mystring = ''
    for i in range(len(inputList)):
        if i < len(inputList) - 2:
            mystring = mystring + str(inputList[i]) + ", "
        elif i == len(inputList) - 2:
            mystring = mystring + str(inputList[i]) + ", and "
        else:
            mystring = mystring + str(inputList[i])

    return mystring


print (printList([]))
print (printList([1]))
print (printList([1,2,3]))






















