
# import sys

# N = int(input())
# N_list = list(map(int, sys.stdin.readline().split()))
# M = int(input())
# M_list = list(map(int, sys.stdin.readline().split()))

# result = [0] * M
# for i in range(M):
#     for j in range(N):
#         if (M_list[j] == N_list[i]):
#             result[j] += 1
#     print(result[j])

# n = int(input())
# arr1 = list(map(int, input().split()))

# dict1 = dict()

# for i in arr1:
#     if i in dict1:
#         dict1[i] += 1
#     else:
#         dict1[i] = 1

# m = int(input())
# arr2 = list(map(int, input().split()))

# for i in arr2:
#     if i in dict1:
#         print(dict1[i], end=' ')
#     else:
#         print(0, end=' ')