# x = list(map(int, input()))
# while x[0] != 0:
#     if (x == x[::-1]): # [::-1] 처음부터 끝까지 -1칸 간격으로(역순)
#         print('yes')
#     else:
#         print('no')
#     x = list(map(int, input()))
        

# 백준 1920
# N = int(input())
# N_num = list(map(int, input().split()))
# N_num.sort() # 오름차순을 해야 mid로 중간값을 비교할때
# # M_num의 값이 N_num의 값에 존재하는지 left, right, mid로 비교할 수 있음
# # -> if, elif, elif 이 세 가지 조건에 해당하지 않으면 없으므로 break
# # 1,2,3,4,5
# M = int(input())
# M_num = list(map(int, input().split()))

# for i in M_num: # M_num의 요소를 하나씩 N_num에 존재하는지 확인
#     left = 0
#     right = len(N_num) - 1 # i와 N의 전체 요소와 비교하기 위해 준비
#     find = False

#     while True: # 3가지 조건에 해당하지 않을때까지, 비교하다 left > right가 된다면
#         # 조건에 없으므로 break 후 print(0)
#         # 숫자가 작다면 mid보다 작으므로 left값이 계속 올라가서 break
#         # 숫자가 크다면 mid보다 크므로 right값이 계속 작아져서 break
#         mid = (left + right) // 2 # 중간값
#         if i == N_num[mid]:
#             print(1)
#             find = True
#             break
#         elif i > N_num[mid]:
#             left = mid + 1
#         elif i < N_num[mid]:
#             right = mid - 1
#         if left > right:
#             break
#     if not find:
#         print(0)

# 2164 백준
# list는 popleft를 할 수 없음
# deque는 가능
# from collections import deque
# import sys
# from collections import deque

# N = int(sys.stdin.readline())
# queue = deque()

# for i in range(1,N+1):
#     queue.append(i)
# while len(queue) > 1:
#     queue.popleft()
#     queue.append(queue.popleft())
# print(queue.pop())


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

# AMC 호텔
# T = int(input())

# for _ in range(T):
#     H, W, N = map(int, input().split())
#     floor = 0
#     room = 0
#     if N % H == 0:
#         floor = H * 100
#         room = N // H
#     else:
#         floor = (N % H) * 100
#         room = 1 + N // H
#     print(floor + room)

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


