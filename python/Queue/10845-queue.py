import sys

N = int(input())

# 홀수일 경우와 짝수일 경우
# 생각
# 이분 탐색
# N // 2 가 홀 or 짝일 경우
# left와 right 값
# left일 경우 +1
# right일 경우 -1
left = 0
right = len(N)
N_list = [0] * N
for i in range(N):
    M = (left+right) // 2
    if M > left:
        left -= 1
    elif M < left:
        right += 1
    if M == 0:
        break 