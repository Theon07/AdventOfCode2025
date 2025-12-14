
def is_roll(a):
    return 1 if a == '@' else 0

def count_neighbours(grid, r, c, i, j):
    
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
count = 0    

for i,_ in enumerate(grid):
    for j,_ in enumerate(grid[i]):
        count += count_neighbours(grid, len(grid)-1, len(grid[0])-1, i, j)


print(count)