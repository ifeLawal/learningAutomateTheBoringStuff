# take a 2 dimensional grid print 
# print it down and right

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

try:
    for i in range(len(grid[0])):
    # get length of the horizontal size of the list
        for j in range(len(grid)):
        # get the length of the vertical size of the list
            print(grid[j][i], end='')
        print('\n')
except IndexError:
    print('No value in your list')
