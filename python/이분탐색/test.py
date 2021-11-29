import sys
N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))
start, end = 1, max(tree)

while start <= end:
    mid = (start+end) // 2
    count = 0
    for i in tree:
        if i >= mid:
            count += i - mid
            if count >= M:
                break
    if count >= M:
        start = mid + 1
    else:
        end = mid - 1