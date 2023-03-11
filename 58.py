N, X, Y = map(int, input().split())

# N＞= X + Y
# N = (X+Y) = odd or even

if N < abs(X) + abs(Y):
    print("No")
    exit()
else:
    if X == 0 and Y == 0:
        if N % 2 == 0:
            print("Yes")
        else:
            print("No")
    elif N % 2 == (X + Y) % 2:
        print("Yes")
        exit()
    else:
        print("No")