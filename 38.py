N, Q = map(int, input().split())
A = list(map(int, input().split()))

question = [list(map(int, input().split())) for _ in range(Q)]

B = [0] * (N + 1)

for i in range(1, N + 1):
    B[i] = B[i - 1] + A[i - 1]

for i in range(Q):
    l = question[i][0]
    r = question[i][1]
    print(B[r] - B[l-1])