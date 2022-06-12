from collections import deque
from sys import stdin

# read = stdin.readline
# N이 정점개수, M이 간선개수, V가 시작정점
# N, M, V = map(int, read().split())

n , m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0],[0, 0, -1, 1]

def bfs(a,b):
    if maze[a][b] == 1:
        queue = deque([[a, b]])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            px = x + dx[i]
            py = y + dx[i]
            if 0 <= x < n and 0 <= y < m and 0 <= px < n and 0 <= py < m:
                if maze[px][py] == 1:
                    maze[px][py] = maze[x][y]
                    queue.append([px, py])

bfs(0,0)
print(maze[n-1][m-1])