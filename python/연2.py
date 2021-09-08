# N과 M
# N, M = map(int, input().split())
# solve = []


# def back(x):
#     if x == M:
#         for i in solve:
#             print(i, end=' ')
#         print()
#         return
#     for i in range(1, N+1):
#         if i not in solve:
#             # if i not in solve로 같은 수 중복 방지
#             solve.append(i)
#             back(x + 1)
#             solve.pop()


# back(0)

# back(0)으로 함수 호출
# -> solve[1]
# -> 재귀함수를 만나 다시 처음부터 시작, x== 1로 변함
# -> solve[1,2]가 들어옴 -> 재귀로 다시 처음으로 돌아감 x==2
# -> 첫번째 if문에 부합하므로 solve에 들어있는 1 2가 출력됨, return으로 solve[2]를 돌려줌, -->하나의 재귀가 끝남
# -> solve.pop()을 통해 2가 사라지고 solve[1]만 남음
# -> for문은 돌아가는 상태이므로 solve에 없는 [3]이 들어갈차례
# -> solve[1,3]이 됨 -> x는 다시 2인 상태(why? 바로 전의 재귀가 종료되었으므로 x==1인 상태의 재귀함수인 상태임)
# -> 위 결과의 반복으로 1 4 까지 출력
# -> 1로 시작하는 모든 재귀가 종료되면서 solve.pop을 통해 빈 list로 돌아옴
# -> back(x+1)이 결국 이중 for문 역활을함(재귀==이중for문)
# -> 2,3,4로 시작하는 백트래킹은 위의과정을 거침

# N과 M(2)
# N, M = map(int, input().split())
# solve = []

# # len = 입력값의 길이(요소의 전체 개수)를 리턴해줌
# # range = 필요한 만큼의 숫자를 만들어냄 -> for문과 같이 사용


# def back(x):
#     if x == M:
#         for i in solve:
#             print(i, end=' ')
#         print()
#         return
#     for i in range(1, N+1):
#         if i not in solve:
#             # if i not in solve로 같은 수 중복 방지
#             solve.append(i)
#             back(x + 1)
#             solve.pop()
# back(0)

# N, M = map(int, input().split())
# num = []


# def back(x):
#     if len(num) == M:
#         # 1. 방법 : print(' '.join(map(str, num)))
#         #  return
#         # 2. 방법
#         for i in num:
#             print(i, end=' ')
#         print()
#         return
#     for i in range(x, N+1):
#         if i not in num:
#             num.append(i)
#             # back i + 1로 x의 값을 1씩 늘려주면서
#             # 자동으로 오름차순/
#             back(i+1)
#             num.pop()


# back(1)

# RGB 문제
# n = int(input())
# p = []
# for i in range(n):
#     p.append(list(map(int, input().split())))
# for i in range(1, len(p)):
#     p[i][0] = min(p[i - 1][1], p[i - 1][2]) + p[i][0]
#     p[i][1] = min(p[i - 1][0], p[i - 1][2]) + p[i][1]
#     p[i][2] = min(p[i - 1][0], p[i - 1][1]) + p[i][2]
# print(min(p[n - 1][0], p[n - 1][1], p[n - 1][2]))
