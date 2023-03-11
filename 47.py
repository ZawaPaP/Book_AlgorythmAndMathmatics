import sys
sys.setrecursionlimit(210000)


N, M = map(int, input().split())

A = [ None ] * M
B = [ None ] * M

for i in range(M):
    A[i], B[i] = map(int, input().split())

G = [list() for i in range(N + 1)]

for i in range(M):
    G[A[i]].append(B[i])
    G[B[i]].append(A[i])

# coloring each points to 1 or 2, initiate to 0
C = [ 0 ] * (N + 1)

def dfs(pos, C, G):
    for i in G[pos]:
        if C[i] == 0:
            C[i] = 3 - C[pos]
            dfs(i, C, G)

for i in range(1, N + 1):
    if C[i] == 0:
        C[i] = 1
        dfs(i, C, G)

ans = True
for i in range(M):
    if C[A[i]] == C[B[i]]:
        ans = False

if ans == True:
    print("Yes")
else:
    print("No")