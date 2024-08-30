grid = [
    ['.','.','O','O','.','O','O','.','.'],
    ['.','0','0','0','0','O','O','O','.'],
    ['.','0','0','0','0','0','0','0','0','.'],
    ['.','.','0','O','O','O','O','.','.']
]
for verticalCoor in range(len(grid)):
    print()
    for horizontalCoor in range(len(grid[verticalCoor])):
        print(grid[verticalCoor][horizontalCoor],end='')
