grid = [list(x.strip()) for x in open(0)]


count = 0
for i,_ in enumerate(grid):
    for j in range(len(grid[i])):
        if grid[i][j] == '.' and grid[i-1][j] in 'S|':
            grid[i][j] = '|'
        if grid[i][j] == '^' and grid[i-1][j] in 'S|':
            count += 1
            if j > 0:
                grid[i][j-1] = '|'
            if j < len(grid[i])-1:
                grid[i][j+1] = '|'
            
for g in grid:
    print(''.join(g))
        
print(count)