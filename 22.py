n = int(input())
A = list(map(int, input().split()))

cnt = [0 for i in range(100000)]
c50000 = 0

for i in range(0, len(A)):
    cnt[A[i]] += 1

ans = 0

for j in range(0, 50000):
    ans += cnt[j] * cnt[100000 - j]
    ans += cnt[50000] * cnt[50000 - 1] // 2

print(cnt)