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

