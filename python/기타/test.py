# 공장의 비용문제로 두개의 조립라인이 하나의 부품공급라인을 공유한다.

# 부품라인은 두개의 조립라인에 부품을 조립순서대로 공급해 준다.

# 부품 중 각각의 조립라인에 중복되는 부품은 단 1개만 존재한다.

# 아래 그림과 같이 부품라인 순서대로 양쪽 조립라인에 부품을 조달할 수 있으며, 모든 부품이 조달되면 정상적으로 조립이 된다.
# 두 조립라인 모두 성공적으로 조립이 되면 ‘1’ , 조립되지 않으면 ‘0’을 출력하라.

# [제약조건]

# -조립라인의 부품수는 50개를 넘기지 않는다.

# -부품번호는 1=< N =< 100

# -각 조립라인에 중복되는 부품은 단 1개 존재한다.

import sys

n = int(sys.stdin.readline())

top = list(map(int, sys.stdin.readline().split()))
bottom = list(map(int, sys.stdin.readline().split()))
line = list(map(int, sys.stdin.readline().split()))

print(n)

for i in range(3):
    if len(top) == n:
        print(1)
    elif len(bottom) == n:
        print(1)
    elif len(line) == n:
        print(1)
    else:
        print(0)


# 부품공급라인 
# 조립라인1
# 조립라인2


# time_a = 0
# time_b = 0
# work_a = 0
# work_b = 0

# for i in range(n-1):
#     if n == 1:
#         break
#     time_a = min(line[i][0] + work_a, line[i][1] + line[i][3] + work_b)
#     time_b = min(line[i][1] + work_b, line[i][0] + line[i][2] + work_a)
#     work_a = time_a
#     work_b = time_b

# time_a += finish[0]
# time_b += finish[1]

# print(min(time_a, time_b))