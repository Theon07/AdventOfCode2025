ranges = [list(map(int, rng.split('-'))) for rng in input().split(',')]

res = 0
print(len(ranges))
for i,v in enumerate(ranges):
    s, e = v
    print(len(ranges)-i-1)
    for j in range(s, e+1):
        a = str(j)
        l = len(a)
        for block_size in range(l//2,0,-1):
            if l % block_size == 0:
                blocks = [a[x:x+block_size] for x in range(0,l,block_size)]
                if len(set(blocks)) == 1:
                    res += j
                    break

print("ans", res)
            

            

# print(res)