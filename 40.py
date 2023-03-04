N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = [int(input()) for _ in range(M)]

L = [0] * (N)

L[1] = A[0]
for i in range(2, N):
    L[i] = L[i - 1] + A[i - 1]
ans = 0
for j in range(M - 1):
    l = B[j]
    r = B[j + 1]
    ans += abs(L[l - 1] - L[r - 1])

print(ans)