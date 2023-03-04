N = int(input())

L = [list(map(int, input().split())) for _ in range(N)]
    
ans = 100000000
for i in range(N):
    for j in range(i+1, N):
        tmp = ((L[i][0] - L[j][0])**2 + (L[i][1] - L[j][1])**2)**0.5
        ans = min(ans, tmp)

print(ans)