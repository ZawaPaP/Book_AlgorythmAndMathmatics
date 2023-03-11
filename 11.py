N = int(input())

prime = [True] * (N + 1)

for i in range(2, int(N**0.5) + 1):
    if prime[i] == True:
        for j in range(2, (N // i + 1)):
            prime[i * j] = False

cnt = []
# deduct the  of 0, 1
for i in range(2, len(prime)):
    if prime[i] == True:
        cnt.append(i)
print(" ".join(str(c) for c in cnt))
