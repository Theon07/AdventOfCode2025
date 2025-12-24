import heapq as hq

points = [(int(x),int(y),int(z)) for x,y,z in [line.strip().split(',') for line in open(0)]]

def dist(a,b):
    return sum((x-y)**2 for x,y in zip(a,b))

h = []

for i,a in enumerate(points):
    for j,b in enumerate(points[i+1:]):
        d = dist(a, b)
        item = (d, i, i+1+j)

        if len(h) < 1000:
            hq.heappush_max(h, item)
        else:
            if d < h[0][0]:
                hq.heapreplace_max(h, item)

pairs = sorted(h)

parent = [x for x in range(len(points))]
size = [1] * len(points)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    pa = find(a)
    pb = find(b)
    if pa == pb:
        return
    
    if size[pa] < size[pb]:
        pa,pb = pb,pa

    parent[pb] = pa
    size[pa] += size[pb]
    size[pb] = 0

for _,a,b in pairs:
    union(a, b)

res = 1
for s in sorted(size)[-3:]:
    res*=s

print(res)