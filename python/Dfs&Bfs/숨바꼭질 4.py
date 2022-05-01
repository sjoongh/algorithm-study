# 수빈이는 동생과 숨바꼭질 현재 N(0 <= N <= 100000)
# 동생은 점 K(0 <= K <= 100000)에 존재함
# 만약 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동한다.
# 순간이동 한다면 1초 후에 2*x의 위치로 이동
# 수빈이가 동생을 찾을 수 있는 가장 빠른 시간은 몇 초 후?

# 출력 : 어떻게 이동해야 하는지 공백으로 구분
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
visited = [0] * 100001
check = [0] * 100001

def move(now):
    data = []
    tmp = now
    for _ in range(visited[now]+1):
        data.append(tmp)
        tmp = check[tmp]
    print(' '.join(map(str, data[::-1])))

def bfs():
    q = deque()
    q.append(n)
    while q:
        now = q.popleft()
        if now == k:
            print(visited[now])
            move(now)
            return
        for next_node in (now-1, now+1, now*2):
            if 0 <= next_node <= 100000 and visited[next_node] == 0:
                visited[next_node] = visited[now] + 1
                q.append(next_node)
                check[next_node] = now
bfs()

