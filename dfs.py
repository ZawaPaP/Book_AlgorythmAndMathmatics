import sys

def dfs(pos, G, visited):
    visited[pos] = True
    for i in G[pos]:
        if visited[i] == False:
            dfs(i, G, visited)

sys.setrecursionlimit(120000)

N, M = map(int, input().split())
A = [ None ] * M
B = [ None ] * M

for i in range(M):
    A[i], B[i] = map(int, input().split())
    
G = [list() for i in range(N + 1)]
for i in range(M):
    G[A[i]].append(B[i])
    G[B[i]].append(A[i])

visited = [ False ] * (N + 1)
dfs(1, G, visited)

answer = True
for i in range(1, N + 1):
    if visited[i] == False:
        answer = False
if answer == True:
    print("connected")
else:
    print("not connected")
