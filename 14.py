N = int(input())
L = list(map(int, input().split()))


def gcd(A, B):
    while A >= 1 and B >= 1:
        if A > B:
            A = A % B
        else:
            B = B % A
    
    if A > B:
        return A
    else:
        return B

tmp = L[0]
sum = L[0]
for i in range(1, N):
    tmp = gcd(tmp, L[i])
    sum = sum * L[i] // tmp
    tmp = sum
print(sum)