N = int(input())

flag = False

for i in range(1, 60):
    if N == 2**(i) - 1:
        flag = True

if flag == True:
    print("Second")
else:
    print("First")