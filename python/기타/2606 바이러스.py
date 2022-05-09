N = int(input())
M = int(input())

visited = [0] * (N+1)
graph = [[] * N for _ in range(N+1)]
cnt = 0

for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(num):
    # num = [1, ?] 1과 연결된 숫자가 들어옴
    # todo : ?의 숫자가 어디와 연결되었는지 경우의 수 count
    # todo2 : 만약 ?의 숫자가 이후에 들어오는 ?2와 중복될경우 제외
    # --> 이를 위해서는 list형식으로 담고 나중에 반복문 돌려서 없애줘야할듯 or set으로 구현
    global cnt
    visited[num] = 1
    for i in graph[num]:
        if visited[i] == 0:
            dfs(i)
            cnt += 1


dfs(1)
print(cnt)

