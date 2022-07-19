import sys
N, M = map(int, input().split())
len = [int(sys.stdin.readline()) for _ in range(N)]
start, end = 1, max(len)

while start <= end:
    mid = (start + end) // 2
    lines = 0
    for i in len:
        lines += i // mid
    if lines >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)