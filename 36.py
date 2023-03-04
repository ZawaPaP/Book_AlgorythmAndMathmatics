import math 

A, B, H, M = map(int, input().split())

Ax = A * math.sin(math.radians(H * 30 + 0.5 * M))
Ay = A * math.cos(math.radians(H * 30 + 0.5 * M))

Bx = B * math.sin(math.radians(M * 6))
By = B * math.cos(math.radians(M * 6))

dist = math.sqrt((Ax - Bx)**2 + (Ay - By)**2)

print ("%.12f" % dist)