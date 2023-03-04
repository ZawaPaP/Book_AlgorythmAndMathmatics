import math
x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())

dist = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

if dist > r1 + r2:
    print(5)
elif dist == r1 + r2:
    print(4)
elif dist < r1 + r2:
    if r1 >= r2:
        if dist + r2 < r1:
            print(1)
        elif dist + r2 == r1:
            print(2)
        elif dist + r2 > r1:
            print(3)
    elif r2 > r1:
        if dist + r1 < r2:
            print(1)
        elif dist + r1 == r2:
            print(2)
        elif dist + r1 > r2:
            print(3)