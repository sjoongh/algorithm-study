# 브루트포스 : 조합가능한 모든 조합 비교

# 3 4 1 -> 세로길이, 가로길이, 인벤토리에 가진 블록 수
# 64 64 64 64
# 64 64 64 64
# 64 64 64 63
# 3x4의 집터의 블록 높이

# 1 64 -> 걸린시간, 땅을 고른 높이를 결정해야 하므로 고른 땅의 높이

import sys

# N, M, B
# GROUND

N, M, B = int(sys.stdin.readline().split())

GROUND = [list(map(int, input().split())) for _ in range(N)] # 선언과 동시에 입력받음

# 1. 고른 땅의 높이 결정
# 2. 인벤토리의 블록 유무, 전체 - 가장 많은 숫자를 보유한 높이 == 인벤토리 블록숫자
# --> 아니라면 가장 많은 숫자를 보유한 블록을 빼야함
# 위의 과정 반복으로 1번의 답을 결정하면 될듯?
# 블록을 파는건 2초, 넣는건 1초가 걸림

count = 0
count2 = 0
while True:
    for i in GROUND:
        for j in i:
            if j == max(GROUND):
                count += 1
            elif j == min(GROUND):
                count2 += 1
    range(len(GROUND)) - count == B
        # 정답
    range(len(GROUND)) - count != B
        # 
    range(len(GROUND)) - count == B
        # 정답
    range(len(GROUND)) - count != B
        