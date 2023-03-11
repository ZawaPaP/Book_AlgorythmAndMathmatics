"""
input
N  M
A1 B1
A2 B2

Am Bm
頂点数N、辺M, i番目の辺は頂点数 Ai, Biを結ぶ
"""

N, M = map(int, input().split())
A = [ None ] * M
B = [ None ] * M

for i in range(M):
    A[i], B[i] = map(int, input().split())

# G[i] は頂点 i に隣接する頂点のリスト
G = [list() for i in range(N + 1)]
for i in range(M):
    G[A[i]].append(B[i])
    G[B[i]].append(A[i])

# output
for i in range(1, N + 1):
    output = str(i) + ": {"
    for j in range(len(G[i])):
        if j >= 1:
            output += ","
        output += str(G[i][j])
    output += "}"
    print(output)
