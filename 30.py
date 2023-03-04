N, W = map(int, input().split())

w = N * [0]
v = N * [0]

for i in range(N):
    x, y = map(int, input().split())
    w[i] = x
    v[i] = y

#品物 i の重さは w(i)で、価値は v(i), dpは合計価値

dp = [[0 for _ in range(W + 1)] for _ in range(N)]

for i in range(0, N):
    for j in range(0, W + 1):
        if j < w[i]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i]] + v[i])
print(max(dp[N - 1]))