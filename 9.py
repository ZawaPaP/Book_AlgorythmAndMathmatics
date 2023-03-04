N, S = map(int, input().split())
L = list(map(int, input().split()))

dp = [[False for _ in range(S + 1)] for _ in range(N + 1)]
dp[0][0] = True



for i in range(1, N + 1):
    for j in range(0, S + 1):
        if j - L[i - 1] < 0:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = (dp[i - 1][j]) or (dp[i - 1][j - L[i - 1]]) 

if dp[N][S] == True:
    print("Yes")
else:
    print("No")
    