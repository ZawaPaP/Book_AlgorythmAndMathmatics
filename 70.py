N, K = map(int, input().split())

X = [None] * N
Y = [None] * N

for i in range(N):
    X[i], Y[i] = map(int, input().split())


def check(xl, xr, yl, yr):
    cnt = 0
    for i in range(N):
        if xl <= X[i] and X[i] <= xr and yl <= Y[i] and Y[i] <= yr:
            cnt += 1
    return cnt

ans = 10 ** 19

for i in range(N):
    for j in range(N):
        for k in range(N):
            for l in range(N):
                xl = X[i]
                xr = X[j]
                yl = Y[k]
                yr = Y[l]
                if xr > xl and yr > yl:
                    if check(xl, xr, yl, yr) >= K:
                        tmp = abs(xr - xl) * abs(yr - yl)
                        ans = min(ans, tmp)

print(ans)
