N, M = map(int, input().split())
A = [ None ] * M
B = [ None ] * M

for i in range(M):
    A[i], B[i] = map(int, input().split())

G = [list() for i in range(N + 1)]
for i in range(M):
    G[A[i]].append(B[i])
    G[B[i]].append(A[i])

cnt = [0] * (N + 1)
for i in range(1, N + 1):
    for j in range(len(G[i])):
        if i > G[i][j]:
            cnt[i] += 1

ans = 0
for i in range(1, N + 1):
    if cnt[i] == 1:
        ans += 1
print(ans)
