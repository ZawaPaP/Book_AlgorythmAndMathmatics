N = int(input())

tmp = 0
for i in range(0, N):
    tmp += N / (N - i)

print(tmp)