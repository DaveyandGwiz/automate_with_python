# Creating a 1x4 matrix
matrix = [
    [0, 0, 0, 0, 0 ,0 ,0],
    [0, 0, 0, 0, 0 ,0 ,0],
    [0, 0, 0, 0, 0 ,0 ,0],

]
originalMatrix = matrix
#matrix [0] = [1,1,1,1,1]
print(matrix)
# I want to fill a matrix with integer values in a circulur pattern
# starting with top left and moving right till I work on the inner section

counter = 1

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix[i][j] = counter
        print(matrix)
        counter = counter + 1

print (matrix)
def totalSize(array):
    counter = 0
    for i in array:
        for j in i:
            counter = counter + 1
    return counter

totalSizeOg = totalSize(originalMatrix)
print(totalSizeOg)

totalSizeNew = totalSize(matrix)
print(totalSizeNew)


