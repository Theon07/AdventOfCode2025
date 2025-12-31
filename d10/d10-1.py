import z3

total = 0

for line in open(0):
    line = line.strip()
    if not line:
        continue

    # --- robust parsing ---
    sep1 = line.index(']')
    sep2 = line.index('{')

    buttons_part = line[sep1+1:sep2].strip()
    joltages_part = line[sep2+1:-1]

    buttons = [
        set(map(int, btn[1:-1].split(',')))
        for btn in buttons_part.split()
    ]

    joltages = list(map(int, joltages_part.split(',')))

    # --- Z3 model ---
    o = z3.Optimize()

    vars = [z3.Int(f"n{i}") for i in range(len(buttons))]
    for v in vars:
        o.add(v >= 0)

    for i, joltage in enumerate(joltages):
        o.add(
            z3.Sum(
                vars[b] for b, button in enumerate(buttons) if i in button
            ) == joltage
        )

    o.minimize(z3.Sum(vars))
    o.check()

    m = o.model()
    total += m.eval(z3.Sum(vars)).as_long()

print(total)
