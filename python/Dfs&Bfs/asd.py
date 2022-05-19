# import sys

# input = sys.stdin.readline

# # 행의 개수를 입력 받음
# n = int(input())
# # 2번째 줄부터 n+1번째 줄까지 한 행에 있는 모든 노드를 입력받음
# paint = [list(map(int, input().split())) for _ in range(n)]

# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]

# print(paint)

# while True:
#     print('행 index', end=' ')
#     x = int(input())
#     print('열 index', end=' ')
#     y = int(input())
#     # i = 0
#     # i = 1
#     # i = 2
#     # i = 3
#     for i in range(4):
#         pointX = x + dx[i]
#         pointY = x + dy[i]
#         print(paint[pointX][pointY])
# -------------------------------------


# 값을 입력받음
# n = int(input())
# x, y = 1, 1
# plans = input().split()

# # L, R, U, D 에 따른 이동방향
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# move_types = ['L','R','U','D']

# # 이동계획을 하나씩 확인
# for plan in plans:
#     # 이동 후 좌표 구함
#     for i in range(len(move_types)):
#         if plan == move_types[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]
#         # 공간을 벗어나는 경우 무시
#         if nx < 1 or ny < 1 or nx > n or ny > n:
#             continue
#         # 이동 수행
#         x,y = nx, ny
# print(x, y)


# import sys

# N, V, M = map(int, sys.stdin.readline().split())

# graph = [[0] * (N+1) for _ in range(N+1)]
# visited = [False] * (N+1)

# for i in range(M):
#     x, y = map(int, sys.stdin.readline().split())
#     graph[x][y] = 1
#     graph[y][x] = 1


# def dfs(V):
#     visited[V] = True
#     print(V, end=' ')
#     for i in range(1, N+1):
#         if not visited[i] and graph[V][i] == 1:
#             dfs(V)
# def bfs(V):
#     visited[V] = False
#     queue = V
#     while queue:
#         V = queue.pop(0)
#         print(V, end='')
#         for i in range(N+1):
#             if visited[i] and graph[V][i] == 1:
#                 queue.append(i)
#                 visited[i] = False

# dfs(V)
# print()
# bfs(V)

# from collections import deque

# n , m = map(int, input().split())
# maze = [list(map(int, input())) for _ in range(n)]
# dx, dy = [-1, 1, 0, 0],[0, 0, -1, 1]

# def bfs(a,b):
#     if maze[a][b] == 1:
#         queue = deque([[a, b]])
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             px = x + dx[i]
#             py = y + dy[i]
#             if 0 <= x < n and 0 <= y < m and 0 <= px < n and 0 <= py < m:
#                 if maze[px][py] == 1:
#                     maze[px][py] += maze[x][y]
#                     queue.append([px, py])
# bfs(0,0)
# print(maze[n-1][m-1])


import sys

N, M, V = map(int, sys.stdin.readline().split())
graph = [[0] * (N+1) for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M): # 간선 길이만큼 
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y] = 1
    graph[y][x] = 1
    
def dfs(V): # 깊이, stack, 재귀
    visited[V] = True # 시작 정점은 방문 표시후 바로 출력
    print(V, end=' ')
    for i in range(1, N+1):
        if not visited[i] and graph[V][i] == 1:
            dfs(i)
            
def bfs(V): # 너비, queue
    visited[V] = False
    print(V)
    print([V])
    print(visited[V])
    queue = [V]
    while queue:
        V = queue.pop(0)
        print(V, end=' ')
        for i in range(1, N+1):
            if visited[i] and graph[V][i] == 1:
                queue.append(i)
                visited[i] = False

dfs(V)
print()
bfs(V)

# AMC호텔
# T = int(input())

# for i in range(T):
#     H, W, N = map(int, input().split())
#     floor = 0
#     room = 0
#     if N % H == 0: # N을 H로 나누었을때 0일 경우(예외)
#         floor = H * 100 # 층
#         room = N // H # 호수
#     else: # 0으로 안나누어 떨어지면 층수보다 N값이 많으므로
#         floor = (N % H) * 100 # N으로 H를 나눈 나머지값 * 층
#         room = 1 + N // H # 0으로 안나누어 떨어지면 +1만큼 해줘야 올바른 호수
#     print(floor + room)

# 나이순 정렬
# import sys

# N = int(sys.stdin.readline())
# people = []
# for i in range(N):
#     people.append(list(sys.stdin.readline().split()))
# people.sort(key=lambda x: int(x[0]))
# # people는 이중배열인 상태[age][name]이 들어가있음
# # 위 람다식과 동일함 [1]로 하면 name으로 정렬됨
# # def ladmbda(x):
#     # return x[0]
# for i in range(N):
#     print(people[i][0], people[i][1])

# import sys

# N, M, V = map(int, sys.stdin.readline().split())
# graph = [[0] * (N+1) for _ in range(N+1)]
# visited = [False] * (N+1)

# for _ in range(M):
#     x, y = map(int, sys.stdin.readline().split())
#     graph[x][y] = 1
#     graph[y][x] = 1

# def dfs(V):
#     visited[V] = False
#     print(V, end=' ')
#     for i in range(1, N+1):
#         if not visited[i] and graph[V][i] == 1:
#             dfs(i)
            
# def bfs(V):
#     visited[V] = True
#     queue = visited[V]
#     while queue:
#         V = queue.pop(0)
#         print(V, end=' ')
#         for i in range(1, N+1):
#             if visited[i] and graph[V][i] == 1:
#                 queue.append(i)
#                 visited[i] = False
                
# dfs(V)
# print()
# bfs(V)
