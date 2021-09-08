 # from sys import stdin

# read = stdin.readline
# N이 정점개수, M이 간선개수, V가 시작정점
# N, M, V = map(int, read().split())
# # graph = [[0]*(N+1)]*(N+1) # 연산자로 이중배열 생성
# # graph = [[0 for col in range(N+1)] for row in range(N+1)] # for문으로 이중배열 생성
# # graph = [[0]*(N+1) for _ in range(N+1)] # 연산자와 for문으로 이중배열 생성
# graph = [[0] * (N+1) for _ in range(N+1)]  # 이중배열 생성
# 방문한 곳을 다시 방문하지 않게 visited라는 1차원행렬을 만듬
# visited = [False] * (N+1) # [False] 한행(5개) 생성

# 간선이 양방향이기 때문에 둘 다 선택해야 된다(문제에서 양방향임) --> (1,4) & (4,1) 선택

# for _ in range(M):
#     x, y = map(int, input().split())
#     graph[x][y] = 1
#     graph[y][x] = 1

# def dfs(V):
#     visited[V] = True # 방문했을떄 False로 되어있는 것을 True로 바꿔줌
#     print(V, end=' ') # 처음 방문한 지점 출력
#     for i in range(1, N+1): # 
#         if not visited[i] and graph[V][i] == 1:
#             dfs(i)

# def bfs(V): 
#     visited[V] = False
#     queue = [V] # dfs와 반대로 방문을 했을 경우 0으로 바꿔줌 && 선입선출
#     while queue: # queue에는 [1]이 들어있음 즉 1번 돌아감, 근데 밑에서 [2],[3],[4]가 추가됨 즉 3번 더 돔
#         V = queue.pop(0) # False로 바뀌어진 값을 빼내서 그대로 출력
#         print(V, end=' ') # while문이 총 4번 돌아가므로 4개의 index 출력함 
#         for i in range(1, N+1):
#             if visited[i] and graph[V][i] == 1:
#                 queue.append(i)
#                 visited[i] = False
#                   1 2 / 1 3 / 1 4 / 2 4 / 3 4
# 둘 다에 True 표시
# 예제 입력 부분에서 작은 숫자를 앞에다가 썻지만
# 만약 큰 숫자가 앞에 나올 경우 (1,4)가 아닌 (4,1)을 썼을 경우도
# 결과는 같기 때문에 둘 다에 표시
# for _ in range(N+1):
#     x,y = map(int, input().split())
#     graph[x][y] = 1
#     graph[y][x] = 1


# 상하좌우 델타

# n = int(input())
# x, y = 1, 1
# plans = input().split()

# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# move_types = ['L','R','U','D']

# for plan in plans:
#     for i in range(len(move_types)):
#         if plan == move_types[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]
#         if nx < 1 or ny < 1 or nx > n or ny > n:
#             continue
#         x, y = nx, ny
        
# print(x, y)

# 방법 2
# import sys

# n = int(sys.stdin.readline)

# paint = [list(map(int, input().split())) for _ in range(n)]

# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]

# print(paint)

# while True:
#     print('행', end=' ')
#     x = int(input())
#     print('열', end=' ')
#     y = int(input())
#     for i in range(4):
#         pointX = x + dy[i]
#         pointY = y + dy[i]
#         print(paint[pointX][pointY])

# 방법3
# from collections import deque

# n,m = map(int,input().split())
# maze = [list(map(int,input())) for _ in range(n)]
# dx, dy = [-1,1,0,0], [0,0,-1,1]

# def check(x,y): #바깥 범위인지 확인
#     if 0<=x<n and 0<=y<m:
#         return True
#     return False

# def bfs(a,b):
#     if maze[a][b] == 1: #1이면 미방문이라고 판단
#         queue = deque([[a,b]])
#         while queue: 
#             x,y = queue.popleft()
#             for i in range(4): #동서남북
#                 nx, ny = x + dx[i], y + dy[i]
#                 if check(nx,ny): #바깥 범위 배제
#                     if maze[nx][ny] == 1: # 방문하지 않은 곳이라면
#                         maze[nx][ny] += maze[x][y] # 1칸 이동할 때 이전 값 더해주기
#                         queue.append([nx,ny])

# bfs(0,0)
# print(maze[n-1][m-1])

# from collections import deque # deque 가져옴

# n, m = map(int, input().split())
# maze = [list(map(int, input())) for _ in range(n)] # 2차원 배열 만듬
# dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
# # L, R, U, D

# def bfs(a,b):
#     if maze[a][b] == 1: # 1이면 미방문이라고 판단
#         queue = deque([[a, b]])
#         while queue:
#             # 기존의 pop은 맨끝의 요소를 빼서 반환했다면
#             # popleft는 맨왼쪽 즉 가장 먼저 들어간 요소를 빼서 반환함
#             x, y = queue.popleft()
#             for i in range(4): # 동서남북
#                 nx, ny = x + dx[i], y + dy[i] # 동서남북 중 어느 곳으로 이동할지 반복문 돌면서 결정
#                 if 0 <= x < n and 0 <= y < m: # 바깥범위배제
#                     if maze[nx][ny] == 1: # 동서남북 검사해서 1이 존재한다면
#                         maze[nx][ny] += maze[x][y] # 1칸 이동할때 and 이전 값 더해줌 -> 이유 : 그 영역으로 움직여야 하므로
#                         queue.append([nx, ny]) # nx,ny에 값 추가
# bfs(0, 0) # 미로의 시작은 [0][0] 
# print(maze[n-1][m-1]) # 지나야하는 최소의 칸 수를 출력
# -1을 하는 이유는 index가 0부터 시작했기때문

# from collections import deque

# n, m = map(int, input().split())
# maze = [list(map(int, input())) for _ in range(n)]
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def check(x,y): #바깥 범위인지 확인
#     if 0<=x<n and 0<=y<m:
#         return True
#     return False
# def bfs(a, b):
#     if maze[a][b] == 1:
#         queue = deque([[a, b]])
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= x < n and 0 <= y < m and 0 <= nx < n and 0 <= ny < m:
#                 if maze[nx][ny] == 1:
#                     maze[nx][ny] += maze[x][y]
#                     queue.append([nx, ny])
# bfs(0, 0)
# print(maze[n-1][m-1])


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

