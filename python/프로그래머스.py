
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

# print(solution(1, 30))


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

