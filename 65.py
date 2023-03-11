H, W = map(int, input().split())

if H == 1 or W == 1:
    print(1)
    exit()

if W % 2 == 0:
    print(H * W // 2)
else:
    if H % 2 == 0:
        print((H // 2) * (W // 2) + (H // 2) * (W //2 + 1))
    else:
        print((H // 2) * (W // 2) + (H // 2 + 1) * (W //2 + 1))
