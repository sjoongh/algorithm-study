# stack 문제 -------------------

# .split(문자열 나누기) 공백을 기준으로 나눠줌
# .split()를 하면 자동으로 list type이 된다

import sys
N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    word = sys.stdin.readline().split()
    order = word[0]

    if order == "push":
        value = word[1]
        stack.append(value)
    elif order == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif order == "size":
        if len(stack) != 0:
            print(len(stack))
        else:
            print(0)
    elif order == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif order == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
