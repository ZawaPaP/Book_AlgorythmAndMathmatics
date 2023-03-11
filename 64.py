N, K = map(int, input().split())
A = list(map(int, input().split()))

if sum(A) > K:
    print("No")
elif K % 2 == sum(A) % 2:
    print("Yes")
else:
    print("No")