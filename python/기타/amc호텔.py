T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    floor = 0
    room = 0
    if N % H == 0:
        floor = H * 100
        room = N // H
    else:
        floor = (N % H) * 100
        room = 1 + N // H
    print(floor + room)