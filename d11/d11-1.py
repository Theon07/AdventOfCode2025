from functools import lru_cache


graph = {src: dsts.split() for line in open(0) for src, dsts in [line.strip().split(": ")]}


@lru_cache(None)
def count_paths(node):
    if node == "out":
        return 1
    return sum(count_paths(nxt) for nxt in graph.get(node, []))

print(count_paths("you"))
