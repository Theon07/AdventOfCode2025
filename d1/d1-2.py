instructions = [ [l[0],int(l[1:])] for l in [line.strip() for line in open(0)] ]

dial ,count = 50, 0

for dr, rot in instructions:
    if dr == "L":
        for i in range(rot):
            dial-=1
            if dial == 0:
                count+=1
                dial = 100
            # if dial < 0:
            #     dial = 99
    if dr == "R":
        for i in range(rot):
            dial+=1
            if dial == 100:
                count+=1
            if dial > 100:
                dial = 1

print(count)