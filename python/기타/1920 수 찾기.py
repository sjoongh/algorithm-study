# 백준 1920
# N = int(input())
# N_num = list(map(int, input().split()))
# N_num.sort() # 오름차순을 해야 mid로 중간값을 비교할때
# # M_num의 값이 N_num의 값에 존재하는지 left, right, mid로 비교할 수 있음
# # -> if, elif, elif 이 세 가지 조건에 해당하지 않으면 없으므로 break
# # 1,2,3,4,5
M = int(input())
M_num = list(map(int, input().split()))

for i in M_num: # M_num의 요소를 하나씩 N_num에 존재하는지 확인
    left = 0
    right = len(N_num) - 1 # i와 N의 전체 요소와 비교하기 위해 준비
    find = False

    while True: # 3가지 조건에 해당하지 않을때까지, 비교하다 left > right가 된다면
        # 조건에 없으므로 break 후 print(0)
        # 숫자가 작다면 mid보다 작으므로 left값이 계속 올라가서 break
        # 숫자가 크다면 mid보다 크므로 right값이 계속 작아져서 break
        mid = (left + right) // 2 # 중간값
        if i == N_num[mid]:
            print(1)
            find = True
            break
        elif i > N_num[mid]:
            left = mid + 1
        elif i < N_num[mid]:
            right = mid - 1
        if left > right:
            break
    if not find:
        print(0)
