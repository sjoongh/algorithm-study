N = int(input())
M = int(input())

visited = [0] * (N+1)
graph = [[] * N for _ in range(N+1)]
cnt = 0

for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b) # graph에 역순 저장
    graph[b].append(a) # graph에 역순 저장

def dfs(num):
    global cnt
    visited[num] = 1
    for i in graph[num]:
        if visited[i] == 0:
            dfs(i)
            cnt += 1


dfs(1) # 1
print(cnt)

