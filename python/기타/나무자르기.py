# 나무 수 N개
# 나무 M미터 필요(가져가야할것),
# 높이H를 지정해야함(높이를 지정하면 톱날이 땅으로부터 h미터 올라감)
# H보다 높은 나무는 잘라짐
# 높이의 최대값 설정

import sys
N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))
start, end = 1, max(tree)
# 나무높이 sort로 정렬 후
# 가장 큰높이가 다음 인덱스와 같아진다면
# -1씩,
mid = (start+end) // 2
for i in range(N):
    if tree[i] > mid:
        tree[i] - 1
    else:
        tree[i] < mid
        tree[i] + 1
    
