from functools import lru_cache

data = open(0).read().splitlines()

shapes = {}
i = 0
while data[i].endswith(":") and data[i][:-1].isdigit():
    idx = int(data[i][:-1])
    i += 1
    g = []
    while i < len(data) and data[i]:
        g.append(data[i])
        i += 1
    i += 1
    shapes[idx] = {(x, y) for y, r in enumerate(g) for x, c in enumerate(r) if c == "#"}

regions = []
for line in data[i:]:
    if not line:
        continue
    a, b = line.split(":")
    w, h = map(int, a.split("x"))
    cnt = list(map(int, b.split()))
    regions.append((w, h, cnt))

def normalize(s):
    mx = min(x for x, _ in s)
    my = min(y for _, y in s)
    return frozenset((x - mx, y - my) for x, y in s)

def all_orients(s):
    res = set()
    for _ in range(4):
        s = {(y, -x) for x, y in s}
        for f in (1, -1):
            res.add(normalize({(f * x, y) for x, y in s}))
    return res

orients = {k: list(all_orients(v)) for k, v in shapes.items()}
areas = {k: len(v) for k, v in shapes.items()}

def solve(w, h, cnt):
    if sum(cnt[i] * areas[i] for i in range(len(cnt))) > w * h:
        return False

    placements = {}
    for i, c in enumerate(cnt):
        if c == 0:
            continue
        ps = []
        for o in orients[i]:
            maxx = max(x for x, _ in o)
            maxy = max(y for _, y in o)
            for dx in range(w - maxx):
                for dy in range(h - maxy):
                    ps.append(frozenset((x + dx, y + dy) for x, y in o))
        placements[i] = ps

    order = sorted(
        [i for i in range(len(cnt)) if cnt[i] > 0],
        key=lambda i: (len(placements[i]), -areas[i])
    )

    @lru_cache(None)
    def dfs(mask, counts):
        if sum(counts) == 0:
            return True

        for i in order:
            if counts[i] > 0:
                shape = i
                break

        for p in placements[shape]:
            bits = 0
            ok = True
            for x, y in p:
                b = 1 << (y * w + x)
                if mask & b:
                    ok = False
                    break
                bits |= b
            if not ok:
                continue
            nc = list(counts)
            nc[shape] -= 1
            if dfs(mask | bits, tuple(nc)):
                return True
        return False

    return dfs(0, tuple(cnt))

res = 0
for w, h, cnt in regions:
    if solve(w, h, cnt):
        res += 1

print()
print(res)
