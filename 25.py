N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

expec = 0
for i in range(0, N):
  expec += A[i]/3 + B[i]*2 / 3
print(expec)