
def is_roll(a):
    return 1 if a == '@' else 0

def accessiable_roll(grid, r, c, i, j):
    
    if not is_roll(grid[i][j]):
        return 0

    nn = 0
    if i > 0:
        nn += is_roll(grid[i-1][j])
    if j > 0:
        nn += is_roll(grid[i][j-1])
    if i < r:
        nn += is_roll(grid[i+1][j])
    if j < c:
        nn += is_roll(grid[i][j+1])
    if i > 0 and j > 0:
        nn += is_roll(grid[i-1][j-1])
    if i < r and j < c:
        nn += is_roll(grid[i+1][j+1])
    if i > 0 and j < c:
        nn += is_roll(grid[i-1][j+1])
    if i < r and j > 0:
        nn += is_roll(grid[i+1][j-1])

    return nn < 4

grid = [list(x.strip()) for x in open(0)]


def print_grid(grid):
    for i in grid:
        for j in i:
            print(j, end=' ')
        print()


count = 0
prev = -1

while prev != count:
    prev = count
    grid2 = [row[:] for row in grid[:]]
    for i,_ in enumerate(grid):
        for j,_ in enumerate(grid[i]):
            if is_roll(grid[i][j]) and accessiable_roll(grid, len(grid)-1,  len(grid[0])-1, i, j):
                grid2[i][j] = '.'
                count+=1
    
    grid = [row[:] for row in grid2[:]]

# print_grid(grid)
print(count)