# 2164 백준
# list는 popleft를 할 수 없음
# deque는 가능
from collections import deque
import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque()

for i in range(1,N+1):
    queue.append(i)
while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())
print(queue.pop())