banks = [[int(d) for d in x.strip()] for x in open(0)]
joltage = 0

for bank in banks:
    first_part = [int(x) for x in bank[:-1]]
    l = 0
    if len(first_part) > 1:
        l = bank.index(max(first_part))
    if l+1 < len(bank):
        joltage += int(bank[l]+max(bank[l+1:]))

print(joltage)