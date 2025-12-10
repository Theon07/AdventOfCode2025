instructions = [int(line.strip().replace("L", "-").replace("R","")) for line in open(0)]

dial = 50
count = 0

for instruction in instructions:
    dial = (dial+instruction)%100
    if dial == 0:
        count+= 1

print(count)