# 이분탐색 : 특정한 값을 찾아야 할 때 경우의 수를 검색시마다 반으로 줄여 찾음
# 이분탐색의 방식을 사용하되(이분탐색 응용버전이라고 생각)
# 결국엔 배열의 모든 값을 비교해야 하므로 정렬할 필요는 x
# 기존 이분탐색은 정렬이 필수적으로 필요
# 나무 수 N개
# 나무 M미터 필요(가져가야할것),
# 높이H를 지정해야함(높이를 지정하면 톱날이 땅으로부터 h미터 올라감)
# H보다 높은 나무는 잘라짐
# 높이의 최대값 설정

import sys
N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))
start, end = 1, max(tree)

while start <= end:
    mid = (start+end) // 2
    count = 0
    for i in tree:
        # tree의 i 값이 mid보다 큰 경우만
        if i >= mid:
            # count에 현재값-중간값
            count += i - mid
            # 시간초과에 걸리지 않기 위해 count가 M값보다 커지면 반복문 종료
            if count > M:
                break
    #벌목 높이를 이분탐색
    if count >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)
