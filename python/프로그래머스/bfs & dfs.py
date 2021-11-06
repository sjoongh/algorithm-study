
# BFS, DFS 탐색
N,M,V = map(int,input().split())
matrix=[[0]*(N+1) for i in range(N+1)] # 이중배열 만듬 row,col모두 N크기 만큼
for i in range(M):
    a,b = map(int, input().split())
    matrix[a][b]=matrix[b][a]=1 # matrix[a][b] 전부 1로 초기화ㅏ
visit_list=[0]*(N+1) # row생성

def dfs(V):
    visit_list[V]=1 # 1로 초기화
    print(V, end=' ') 
    for i in range(1, N+1):
        if(visit_list[i] == 0 and matrix[V][i] == 1):
            dfs(i)

def bfs(V):
    queue=[V]
    visit_list[V] = 0
    while queue:
        V=queue.pop(0)
        print(V, end=' ')
        for i in range(1, N+1):
            if(visit_list[i] == 1 and matrix[V][i] == 1):
                queue.append(i)
                visit_list[i] = 0
dfs(V)
print()
bfs(V)