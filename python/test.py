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

# 이항계수
# from math import factorial
# N, K = map(int, input().split())
# B = factorial(N) // (factorial(K) * factorial(N-K))
# print(B)

# 나이순 정렬
# import sys

# N = int(sys.stdin.readline())
# people = []
# for i in range(N):
#     people.append(list(sys.stdin.readline().split()))
# people.sort(key=lambda x: int(x[0]))
# # people는 이중배열인 상태[age][name]이 들어가있음
# # 위 람다식과 동일함 [1]로 하면 name으로 정렬됨
# # def ladmbda(x):
#     # return x[0]
# for i in range(N):
#     print(people[i][0], people[i][1])

# import sys
# N = int(sys.stdin.readline())
# # 1. []로 배열하나 생성해놓음
# people = []
# for i in range(N):
#     # 2. 1에서 만든 []안에 []를 넣어서 이중배열을 만들어줌
#     people.append(list(sys.stdin.readline().split()))
#     print(people)

# people.sort(key=lambda x: int(x[0]))

# for i in range(N):
#     print(people[i][0], people[i][1])

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

# 백준 11718 그대로 출력하기
while True :
    try :
        print(input())
    except EOFError:
        break


# import sys
# N, M = map(int, input().split())
# len = [int(sys.stdin.readline()) for _ in range(N)]
# start, end = 1, max(len)

# while start <= end:
#     mid = (start + end) // 2
#     lines = 0
#     for i in len:
#         lines += i // mid
#     if lines >= N:
#         start = mid + 1
#     else:
#         end = mid - 1
# print(end)