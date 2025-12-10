ranges = [list(map(int, rng.split('-'))) for rng in input().split(',')]

res = 0

for i in ranges:
    s, e = i
    for j in range(s, e+1):
        a = str(j)
        if a[:len(a)//2] == a[len(a)//2:]:
            res += j
            

print(res)
    