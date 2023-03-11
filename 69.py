a,b,c,d = map(int, input().split())

ans = max(d * b, a * c, a * d, b * c)
print(ans)