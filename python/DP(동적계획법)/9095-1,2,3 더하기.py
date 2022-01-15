# 방법 1.
# n은 양수이며 11보다 작은 수 이다.
t = int(input())

num = [1,2,4]
# 1,2,3을 각각 range만큼 돌린다음
# 돌아갈때 answer값이 되는 순간만 count

for i in range(3, 10):
    num.append(num[i-3] + num[i-2] + num[i-1])
for _ in range(t):
    n = int(input())
    print(num[n-1])



# 방법 2.
T = int(input())

def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return solution(n-1) + solution(n-2) + solution(n-3)

for i in range(T):
    num = int(input())
    print(solution(num))