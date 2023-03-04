import math

N = int(input())
H = list(map(int, input().split()))
dp = len(H)*[0]

for i in range(0, len(H)):
    if i == 0:
        dp[i] = 0
    elif i == 1:
        dp[i] = abs(H[i] - H[i-1])
    else:
        dp[i] = min(dp[i-2] + abs(H[i] - H[i-2]), dp[i-1] + abs(H[i] - H[i-1]))

print(dp[-1])
