import sys
from collections import deque

N = int(sys.stdin.readline())

dq = deque()

for i in range(N):
    N_list = list(sys.stdin.readline().split())
    if N_list[0] == 'push_front':
        dq.appendleft(N_list[1])
    elif N_list[0] == 'push_back':
        dq.append(N_list[1])
    elif N_list[0] == 'pop_front':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft())
    elif N_list[0] == 'pop_back':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.pop())
    elif N_list[0] == 'size':
        print(len(dq))
    elif N_list[0] == 'empty':
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif N_list[0] == 'front':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    elif N_list[0] == 'back':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])