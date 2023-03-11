import queue

N, M = map(int, input().split())
A = [ None ] * M
B = [ None ] * N

for i in range(M):
    A[i], B[i] = map(int, input().split())

G = [ list() for i in range(N + 1)]
for i in range(M):
    G[A[i]].append(B[i])
    G[B[i]].append(A[i])

dist = [ -1 ] * (N + 1)
Q = queue.Queue()
dist[1] = 0
Q.put(1)

while not Q.empty():
    pos = Q.get()
    for next in G[pos]:
        if dist[next] == -1:
                dist[next] = dist[pos] + 1
                Q.put(next)
    
for i in range(1, N + 1):
    print(dist[i])
