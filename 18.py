n = int(input())
A = list(map(int, input().split()))

dict = {}

for i in A:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

c100 = dict.get(100,0)
c200 = dict.get(200,0)
c300 = dict.get(300,0)
c400 = dict.get(400,0)

print(c100*c400 + c200*c300)