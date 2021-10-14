#   모의고사문제
# def solution(answers):
#     answer = []
#     count1 = 0
#     count2 = 0
#     count3 = 0
#     x = [1, 2, 3, 4, 5]
#     y = [2, 1, 2, 3, 2, 4, 2, 5]
#     z = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

#     range(len(answers)) == answers랑 같음
#     answers=[]
#     for i in range(len(answers)):
#         if answers[i] == x[i % 5]:
#             count1 += 1
#         if answers[i] == y[i % len(y)]:
#             count2 += 1
#         if answers[i] == z[i % len(z)]:
#             count3 += 1

#     mac = max(count1, count2, count3)

#     if mac == count1:
#         answer.append(1)
#     if mac == count2:
#         answer.append(2)
#     if mac == count3:
#         answer.append(3)

#     오름차순 정렬
#     answer.sort()

#     return answer

# solution([[0, 0, 0, 0, 0],
#           [0, 0, 1, 0, 3],
#           [0, 2, 5, 0, 1],
#           [4, 2, 4, 4, 2],
#           [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4])  # -> 이중 for문으로 순서대로 값이 존재하는지 찾아봄 moves에 해당하는 값이 존재하면
#  해당 배열의 값을 0으로 만들고 옮김 -> 반복하다가 -> 마지막 if문에서 요소 2개가 같을경우 지움 그리고 answer += 2
#  break가 없으면 같은 요소가 제거되었음에도 for j문이 계속 돌아가므로 오류가 발생 그러므로 break로 moves의 다음요소를 찾아야함

# 내적, a와b를 곱해서 각 요소들 sum한 값
# def solution(a, b):
#     answer = 0
#     for i in range(len(a)):
#         answer += (a[i] * b[i])

#     return answer

# 로또의 최고 순위와 최저 순위
# x가 산 로또에서 알아볼수 없는 숫자는 0으로구분
# 이 중에서 x가 최고 순위를 받는 경우와 최소 순위를 받는 경우 2가지 구하기
# 비트연산자 & : {0,0} = {0}, {1,1} = {1}, {0,1} = {0}, {0,1} = {0} 이 되는 연산자
# set & set을 하면 중복값만 추출됨 -> 중복값이 없다면 0
# def solution(lottos, win_nums):
#     # set : 중복을 허용하지 않음, 순서가 없음
#     # lottos와 win_nums를 set으로 묶어 중복되는 수를 없앰
#     # {44,1,0,31,25} & {31,10,45,1,6,19}-> &연산자로 중복값 추출 {1, 31} -> cnt=2
#     cnt = len(set(lottos) & set(win_nums))
#     zero = lottos.count(0)  # 0이있으면 count
#     # cnt+zero와 cnt가 0이 될 경우 1로 바꿈
#     return [7-max(cnt+zero, 1), 7-max(cnt, 1)]

# print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))

# 로또 방법 2
# def solution(lottos, win_nums):
#     rank=[6,6,5,4,3,2,1]

#     cnt_0 = lottos.count(0) # 0 카운트
#     ans = 0
#     for x in win_nums:
#         if x in lottos: # lottos에 win_nums와 같은게 있다면
#             ans += 1 # count
#     # list[rank]이기 때문에 count된 수가 높다면 순위가 올라감
#     # 첫번째는 최대로 높은순위, 두번째는 최대로 낮은 순위
#     return rank[cnt_0 + ans], rank[ans]

# x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# for key in x.keys():
#      (key, end=' ')

# a = 3, b = 5,
# 3 + 4 + 5 - 12, return 12,

# 수박 : 3 = "수박수", 4 = "수박수박" 출력
# ''.join(new_answer)


# 2016년 1월1일은 금요일, 2016년 a월 b일은 무슨요일?
# 1->금, 2->토, 3->일, 4->월, 5->화, 6->수, 7->목,->8금
# def solution(a, b):
#     day = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
#     mon = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     # sum(mon[:a-1]) = 시작인덱스 생략,해당 월 -1만큼 전부 더함, 1월 -> 0월이므로 0일만큼 더한값
#     # +b로 1월 30일이면 30 % 7 -> day[2] =  SAT
#     # day[0] = THU
#     return day[(sum(mon[:a-1])+b) % 7]


# print(solution(1, 30))

# stack 문제 -------------------

# .split(문자열 나누기) 공백을 기준으로 나눠줌
# .split()를 하면 자동으로 list type이 된다

# import sys
# N = int(sys.stdin.readline())
# stack = []

# # for 문의 변수를 특별히 사용하지 않을때 _ 사용

# for _ in range(N):
#     word = sys.stdin.readline().split()
#     order = word[0]

#     if order == "push":
#         value = word[1]
#         stack.append(value)
#     elif order == "pop":
#         if len(stack) == 0:
#             print(-1)
#         else:
#             print(stack.pop())
#     elif order == "size":
#         if len(stack) != 0:
#             print(len(stack))
#         else:
#             print(0)
#     elif order == "top":
#         if len(stack) == 0:
#             print(-1)
#         else:
#             print(stack[-1])
#     elif order == "empty":
#         if len(stack) == 0:
#             print(1)
#         else:
#             print(0)


# fibonacci 함수의 해당 위치 값 출력
# cnt0 = [1, 0]
# cnt1 = [0, 1]

# for i in range(2, 41):
#     cnt0.append(cnt0[i-1]+cnt0[i-2])
#     cnt1.append(cnt1[i-1]+cnt1[i-2])
# for _ in range(int(input())):
#     n = int(input())
#     print(cnt0[n], cnt1[n])


# queen
# 인덱스가 행의 값이고 row[index]의 값이 열의 값이다.
# def queen(x): # x와 i가 같으면 행이 같음, but for문을 보면 x와 i가 같을 수 없다
#     for i in range(x): # 인덱스(i)가 행 row[n]값이 열
#         if row[x] == row[i] or abs(row[x] - row[i]) == x - i: # 열이 같거나 대각선이 같으면 false
#             return False # 대각선이 같은 경우는 두 좌표에서 행 - 행 = 열 - 열이 같으면 두개는 같은 대각선상
#     return True

# # 한줄씩 재귀하며 dfs 실행
# def dfs(x):
#     # result를 전역으로 사용 하게함
#     global result

#     if x == N:
#         result += 1
#     # 각행에 퀸 놓기
#     else:
#         for i in range(N): # i는 열번호 0부터 N전까지 옮겨가며 유망한곳 찾음
#             row[x] = i
#             if queen(x): # 행,열,대각선 체크함수 true이면 백트래킹 안하고 계속 진행
#                 dfs(x + 1)

# N = int(input())
# # N크기만큼 행 만듬
# row = [0] * N
# result = 0
# dfs(0)
# print(result)


# 동적계획법(다이나믹 프로그래밍)-상향식,하향식
# 상향식으로 풀어야함
# 상향식 : 제일 작은 인덱스의 수 부터 목표하는 값으로 향함
# 하향식 : 맨위의 값에서 재귀로 제일 작은 인덱스를 향함
# 그리드 : 내가 생각한 최적의 방법이 끝까지 반례없이 적용될때
# 동적계획법 : 가능성을 모두 두고 그 안에 최소값을 찾음
# 모든 경우의 수를 시도해보아야 하므로 동적계획법으로 풀어야함

# n = int(input())
# d = [0] * (n + 1) # d에 계산된 값을 저장해둔다. n+1이라고 한 이유는, 1번째 수는 사실 d[1]이 아니고 d[2]이므로

# for i in range(2, n + 1): # 1을빼고 시작하는 이유는 다음에 계산할 나누기가 1을 뺀값보다 작거나 큼에 따라 어차피 교체되기때문
#     d[i] = d[i - 1] + 1
#     if i % 3 == 0:
            # min(d[i], d[i // 3]) 둘 중 더 작은 수가 d[i]로 들어감
#         d[i] = min(d[i], d[i // 3] + 1) # 1을 더하는 이유는 d는 결과가 아닌 계산한 횟수를 저장하는 것이기 때문
#     if i % 2 == 0:
#         d[i] = min(d[i], d[i // 2] + 1) # d[i]에 더하지 않는 이유는 이미 1을 뺄 때 1을 더해준 이력이 있기때문
# print(d[n])

# import sys

# N = int(sys.stdin.readline())
# lst = []

# for i in range(N):
#     lst.append(sys.stdin.readline().strip) # /strip로 공백제거
# set_lst = set(lst) # set집합으로 중복값제거
# lst = list(set_lst) # 제거된 값 다시 lst로
# lst.sort() # 알파벳 순으로 정렬
# lst.sort(key = len) # key=len으로 요소들의 길이 순으로 정렬

# for i in lst:
#     print(i)


# BFS, DFS 탐색
N,M,V = map(int,input().split())
matrix=[[0]*(N+1) for i in range(N+1)] # 이중배열 만듬 row,col모두 N크기 만큼
for i in range(M):
    a,b = map(int, input().split())
    matrix[a][b]=matrix[b][a]=1 # matrix[a][b] 전부 1로 초기화ㅏ
visit_list=[0]*(N+1) # row생성

def dfs(V):
    visit_list[V]=1 # 1로 초기화
    print(V, end=' ') 
    for i in range(1, N+1):
        if(visit_list[i] == 0 and matrix[V][i] == 1):
            dfs(i)

def bfs(V):
    queue=[V]
    visit_list[V] = 0
    while queue:
        V=queue.pop(0)
        print(V, end=' ')
        for i in range(1, N+1):
            if(visit_list[i] == 1 and matrix[V][i] == 1):
                queue.append(i)
                visit_list[i] = 0
dfs(V)
print()
bfs(V)

# x만큼 간격이 있는 n개의 숫자
def solution(x, n):
    result = []
    for i in range(1, n+1):
        result.appen(x*i)
    return result