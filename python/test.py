# x = list(map(int, input()))
# while x[0] != 0:
#     if (x == x[::-1]): # [::-1] 처음부터 끝까지 -1칸 간격으로(역순)
#         print('yes')
#     else:
#         print('no')
#     x = list(map(int, input()))

# a = int(input())
# for _ in range(a):
#     b = list(input())
#     sum = 0
#     for i in b:
#         if i == '(':
#             sum += 1
#         elif i == ')':
#             sum -= 1
#         if sum < 0:
#             print('NO')
#             break
#     if sum > 0:
#         print('NO')
#     elif sum == 0:
#         print('YES')

# a = int(input())
# for _ in range(a):
#     b = list(input())
#     sum = 0
#     for i in b:
#         if i == '(':
#             sum += 1
#         elif i == ')':
#             sum -= 1
#         if sum < 0: 
#             # sum이 0보다 작을경우 열린괄호보다 닫힌괄호가 많으므로 괄호가 아님
#             # NO를 바로 출력하고 중단시킴
#             print('NO')
#             break
#     if sum > 0: # sum이 0보다 클 경우도 '(' 이 하나더 많으므로 NO
#         print('NO')
#     elif sum == 0: # sum이 0일때만 올바른 답
#         print('YES')

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