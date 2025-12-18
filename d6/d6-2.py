rows = [x.replace('\n', '') for x in open(0)]
cols = list(zip(*rows))

groups = []
group = []

for col in cols:
    if set(col) == {' '}:
        if group:
            groups.append(group)
            group = []
    else:
        group.append(list(col))
if group:
    groups.append(list(group))


res = 0
for gr in groups:
    col = [int((''.join(x)).strip()) for *x,_ in reversed(gr)]
    op = gr[0][-1]
    res+= sum(col) if op == '+' else __import__('math').prod(col)

print(res)
