N = int(input())

# N = 1: 2
# N = 2: 4
# N = 3: 8
# N = 4: 16
# N = 5: 32
# N = 6: 64 
# N = 7: 128
# N = 8: 256
# N = 9: 512
# N = 10: 1024


if N % 4 == 1:
    print(2)
elif N % 4 == 2:
    print(4)
elif N % 4 == 3:
    print(8)
else:
    print(6)
