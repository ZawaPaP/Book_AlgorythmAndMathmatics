n, r = map(int, input().split())

tmp = 1
for i in range(n, n-r, -1):
    tmp = tmp * i

tmp2 = 1
for j in range(r, 0, -1):
    tmp2 = tmp2 * j

print(tmp / tmp2)