import sys

N = int(input())
N_list = list(map(int, sys.stdin.readline().split()))
M = int(input())
M_list = list(map(int, sys.stdin.readline().split()))

result = [0] * M
for i in range(M):
    for j in range(N):
        if (M_list[j] == N_list[i]):
            result[j] += 1
    print(result[j])
