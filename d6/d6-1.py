from math import prod

rows = [line.rstrip('\n') for line in open(0)]
ops = rows[-1].split()
nums = [r.split() for r in rows[:-1]]

s = 0
for j, sym in enumerate(ops):
    col = [int(row[j]) for row in nums]
    s += sum(col) if sym == '+' else prod(col)

print(s)
