points = [list(map(int,line.split(','))) for line in open(0)]

def area(x1,y1,x2,y2):
    return (abs(x1-x2)+1)*(abs(y1-y2)+1)

max_ar = 0


for i,a in enumerate(points):
    for b in points[i+1:]:
        ar = area(*a, *b)
        if ar > max_ar:
            max_ar = ar

print(max_ar)