import queue

R, C = map(int, input().split())
Sy, Sx = map(int, input().split())
Gy, Gx = map(int, input().split())


C = [list() for i in range(R)]
for i in range(R):
    C[i] = (list(input()))

C[Sy - 1][Sx - 1] = 0
#print(C)

Q = queue.Queue()
Q.put([Sy - 1, Sx - 1])

while not Q.empty():
    pos = Q.get()
    next = [[pos[0], pos[1] + 1], [pos[0], pos[1] - 1], [pos[0] + 1, pos[1]], [pos[0] - 1, pos[1]]]
    for i in next:
        if C[i[0]][i[1]] == ".":
            C[i[0]][i[1]] = C[pos[0]][pos[1]] + 1
            Q.put([i[0], i[1]])

print(C[Gy - 1][Gx - 1])
