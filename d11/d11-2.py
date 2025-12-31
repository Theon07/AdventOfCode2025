from functools import lru_cache

graph = {a: b.split() for a, b in (line.strip().split(": ") for line in open(0))}

@lru_cache(None)
def f(node, d, t):
    if node == "out":
        return d and t
    return sum(
        f(n, d or n == "dac", t or n == "fft")
        for n in graph.get(node, [])
    )

print(f("svr", False, False))
