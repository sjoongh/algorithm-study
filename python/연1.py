# ctrl+k, ctrl+c -> 주석
# ctrl+k, ctrl+u -> 주석해제

# num 반대로 출력
'''
num = int(input())
for i in range(num, 0, -1):
print(i)
'''

# 첫번째 정수로 다시 돌아오는 횟수
# tmp = inp = int(input())
# count=0

# while True:
#    ten = tmp//10
#    one = tmp % 10
#    res= ten + one
#    count += 1
#    tmp = int(str(tmp%10) + str(res%10))
#    -> 문자열로 합하고 다시 int형으로 변환
#    if (inp==tmp):
#        break
# print(count)


# 최대, 최소 문제 w

# num=int(input())
# b=list(map(int,input().split()))
# print(min(b), max(b))

# 숫자의 개수

# A, B, C = map(int, input().split())

# num = list(str(A*B*C))

# for i in range(10):
#     print(num.count(str(i)))

# a = input()
# print(ord(a))A
# ord() : 문자의 아스키 코드값을 리턴하는 함수이다.
# chr() : 아스키 코드값 입력으로 받아 그 코드에 해당하는 문자를 출력하는 함수이다.

# 숫자의 합 (방법1)
# n = input()
# print(sum(map(int, input())))

# # 숫자의 합 (방법2)
# n = input()
# nums = input()
# total = 0
# for i in range(n):
#     total += int(nums[i])
# print(total)


# 벌집 문제

# n = int(input())
# cnt = 1
# cnt_six = 6
# count = 1
# while n > cnt:
#     count += 1
#     cnt += cnt_six
#     cnt_six += 6
# print(count)


# 블랙잭문제

# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# sum = 0
# for i in range(n):
#     for j in -range(i+1, n):
#         for k in range(j+1, n):
#             if a[i] + a[j] + a[k] > m:
#                 continue
#             else:
#                 sum = max(sum, a[i] + a[j] + a[k])
#                 -> max가 없으면 list형식으로 값이 sum에 계속 들어감(최대값만 들어가야함)
#                 -> sum= max(sum,)으로 sum에 들어간 전 값이랑 비교해(처음에는 0) 가장 큰 값으로 바꿔줌(반복문이 종료될때까지)
# print(sum)
# 1,2,3,4,5가 존재한다면
# 1,2,3 -> 1,2,4 -> 1,2,5
# 2,3,4 -> 2,3,5 이런식으로 모든 경우의 수를 조합해 가장 큰 max값(m미만)을 sum에 넣어줌


# 재귀함수

# def fibonacci(n):
#     if (n > 1):
#         return n * fibonacci(n - 1)
#     else:
#         return 1


# num = int(input())
# print(fibonacci(num))

# 피보나치

# def fibonacci(n):
#     if (n > 1):
#         return fibonacci(n-1)+fibonacci(n-2)
#     elif (n == 1):
#         return 1
#     elif (n == 0):
#         return 0
# # 9, 8 -> 8, 6 -> 7, 4 -> 6, 2 -> 5, 0 => 55 -> n==0
# num = int(input())
# print(fibonacci(num))

# 하노이 탑
# def hanoi(n, a, b, c):
#     if n == 1:
#         print(a, c)
#     else:
#         hanoi(n-1, a, c, b)
#         print(a, c)
#         hanoi(n-1, b, a, c)

# n = int(input())
# sum = 1
# for i in range(n - 1):
#     sum = sum * 2 + 1
# print(sum)
# hanoi(n, 1, 2, 3)

# N = input()

# for i in range(N):
#     if i + int(N) == N:
#         print(i)
#         break

# # 분해합
# n = int(input())
# x = 0
# for i in range(1, n+1): -> 1~최대값까지
#     if i + sum(map(int, str(i))) == n:
#         print(i)
#         break -> 분해합의 최소값을 구하기 위한 break
# if i == n:
#     print(0) -> 생성자가 없을경우 0


# 덩치 비교
# num = int(input())
# people = []

# for _ in range(num):
#     weight, height = map(int, input().split())
#     people.append((weight, height))
#     -> 변수가 두개라 괄호 두번?
# for i in people: -> i는 현재사람 j는 다음사람
#     rank = 1 -> 덩치 큰 사람수 + 1
#      for j in people:
#         if (i[0] != j[0]) and (i[1] != j[1]): -> 자신을 제외하고 비교
#             if (i[0] < j[0]) and (i[1] < j[1]): -> [0]은 몸무게 [1]은 키
#                 rank += 1
#     print(rank, end=' ')


# 영화감독 숌(브루트 포스)
# num = int(input())
# cnt = 0
# six = 666
# while True:
#     if '666' in str(six):  # six 문자열에 '666'이 있다면?
#         cnt += 1  # cnt += 1
#     if cnt == num:  # cnt == 입력값이 같다면
#         print(six)  # six 출력
#         break
#     six += 1  # six에 '666'이 없다면 1을 더함 while문 반복

# 체스판 다시 칠하기(나중에 또 풀기)
# N, M = map(int, input().split())
# a = []
# board = []

# for _ in range(N):
#     a.append(input())

# for i in range(N-7):
#     for j in range(M-7):
#         x = 0
#         y = 0
#         for k in range(i, i+8):
#             for l in range(j, j+8):
#                 if (l+k) % 2 == 0:
#                     if a[k][l] != 'W':
#                         x += 1
#                     if a[k][l] != 'B':
#                         y += 1
#                 else:
#                     if a[k][l] != 'B':
#                         x += 1
#                     if a[k][l] != 'W':
#                         y += 1
#         board.append(x)
#         board.append(y)
#         -> append 리스트 형태의 data의 마지막에 하나의 값을 추가
# print(min(board))


# 수 정렬하기
# num = int(input())
# m = []
# for j in range(num):
#     n = int(input())
#     m.append(n)

# m = sorted(m)

# for i in range(num):
#     print(m[i])

# sort와 sorted차이
# a1= sorted(a1) 로 같은 변수에 할당가능 -> 원본리스트에 영향을 안줌 copy하는듯
# a2=a1.sort() 로 다른 변수에 할당해야함 -> 원본리스트 자체를 바꿈

# 수 정렬하기2
# import sys -> 인터프리터 제어(EX: cmd or 쉘명령어)

# num = int(input())
# m = []
# for j in range(num):
#     n = int(sys.stdin.readline()) -> input()보다 시간단축, sys.stdin.readline()
#     m.append(n)
# m = sorted(m)

# for i in range(num):
#     sys.stdout.write(str(m[i])+'\n') -> sys.stdout.write()는 줄바꿈 하지않고 출력
#     #print(str(m[i]))로 해도 상관x
