banks = [[int(d) for d in x.strip()] for x in open(0)]
joltage = 0

for bank in banks:
    if len(bank) == 0:
        continue
    res = bank[-12:]
    start = 0
    for i in range(len(res)):
        m = max(bank[start:len(bank)-len(res)+i+1])
        if res[i] != m:
            res[i] = m
        start += bank[start:len(bank)-len(res)+i+1].index(m)+1
    vl = ''.join([str(i) for i in res])
    print(vl)
    joltage += int(vl)

print(joltage)