data = [x.strip() for x in open(0)]
sep = data.index("")

ranges = sorted([list(map(int, x.split('-'))) for x in data[:sep]], key=lambda x: x[0])

ids = sorted([int(x) for x in data[sep + 1:]])

merged = [ranges[0][:]] if ranges else []

for a, b in ranges[1:]:
    prev = merged[-1]
    if prev[1] + 1 < a:
        merged.append([a, b])
    else:
        prev[1] = max(prev[1], b)

count = 0

for s,e in merged:
    count += (e-s+1)

print(count)