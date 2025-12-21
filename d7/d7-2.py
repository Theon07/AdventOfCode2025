from functools import cache
grid = [list(x.strip()) for x in open(0)]

S = [(r,c) for r, row  in enumerate(grid) for c, char in enumerate(row) if char == "S"][0]

@cache
def solve(r,c)->int:
    if r >= len(grid):
        return 1
    if grid[r][c] == '^':
        return solve(r,c-1) + solve(r,c+1)
    else:
        return solve(r+1,c)

print(solve(*S))