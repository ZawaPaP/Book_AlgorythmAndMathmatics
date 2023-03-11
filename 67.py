H , W = map(int, input().split())
num_list = [list(map(int, input().split())) for _ in range(H)]

row = [0 for i in range(H)]
for i in range(H):
    for j in range(W):
        row[i] += num_list[i][j]

col = [0 for i in range(W)]
for i in range(W):
    for j in range(H):
        col[i] += num_list[j][i]

ans = [[0 for j in range(W)] for i in range(H)]

for i in range(H):
    for j in range(W):    
        ans[i][j] = (row[i] + col[j] - num_list[i][j])

for i in range(H):
    print(*ans[i])

