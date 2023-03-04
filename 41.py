T = int(input())
N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]

# 開始、終了での階差数列
ppl = [0] * (T + 1)
for i in range(N):
    ppl[L[i][0]] += 1
    ppl[L[i][1]] -= 1

# 累積和で時間ごとの働いている人数の数列
ans = [0] * (T + 1)
ans[0] = ppl[0]
for j in range(1,T + 1):
    ans[j] = ans[j - 1] + ppl[j]
    
for k in range(len(ans) - 1):
    print(ans[k])