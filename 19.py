n = int(input())
A = list(map(int, input().split()))

dict = {"red":0, "yellow":0, "blue":0}

for i in A:
    if i == 1:
        dict["red"] += 1
    elif i == 2:
        dict["yellow"] += 1
    else:
        dict["blue"] += 1

tmp = 0
cR = dict.get("red", 0)
cY = dict.get("yellow", 0)
cB = dict.get("blue", 0)

if cR >= 2:
    tmp+= cR * (cR - 1) // 2
if cY >= 2:
    tmp+= cY * (cY - 1) // 2
if cB >= 2:
    tmp+= cB * (cB - 1) // 2
print(tmp)