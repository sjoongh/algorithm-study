# visited로 방문한 곳인지 아닌지 판별
# distx와 disty로 회전과 위치 지정
# max값을 구하기 위한 재귀

import sys

N, M = map(int, sys.stdin.readline().split())

arr = [list(map(int, input().split())) for _ in range(N)]

distx = [-1, 0, 1, 0]
disty = [0, 1, 0, -1]
answer = 0
visited = [([0] * M) for _ in range(N)]

maxnum = max(map(max, arr))


def dfs(r, c, idx, total):
    if answer >= total + maxnum * (3 - idx): # 조건에 맞지 않는 결과 반환
        return
    if idx == 3:
        answer = max(answer, total) # 결과값(max) 반환
        return
    else:
        for i in range(4): # 방문
            nr = r + distx[i]
            nc = c + disty[i]
            if 0 <= nr < N and 0 <= nc < M:
                if idx == 1:
                    visited[nr][nc] = 1e
            

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 0, arr[i][j])
        visited[i][j] = False
    