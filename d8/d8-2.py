points = [(int(x),int(y),int(z)) for x,y,z in [line.strip().split(',') for line in open(0)]]

def dist(a,b):
    return sum((x-y)**2 for x,y in zip(a,b))


h = []

for i,a in enumerate(points):
    for j,b in enumerate(points[i+1:]):
        h.append((dist(a, b), i, i+1+j))

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
        return None
    
    if size[pa] < size[pb]:
        pa,pb = pb,pa

    parent[pb] = pa
    size[pa] += size[pb]
    size[pb] = 0
    if len(set(size)) == 2:
        return (a,b)
    return None

for _,a,b in pairs:
    if union(a, b):
        print(points[a][0]*points[b][0])
        break