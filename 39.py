N, Q = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(Q)]

B = [0] * (N + 1)

for i in range(Q):
    l = L[i][0]
    r = L[i][1]
    x = L[i][2]

    B[l - 1] += x
    B[r] -= x

ans = ""
for j in range(1, len(B) - 1):
    if B[j] > 0:
        ans += "<"
    elif B[j] == 0:
        ans += "="
    else:
        ans += ">"

print(ans)
