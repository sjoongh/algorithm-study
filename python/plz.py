def solution(n):
    answer = ''
    num_test1 = 0
    num_test2 = 0
    if n == 1:
        return '1'
    elif n == 2:
        return '2'
    elif n == 3:
        return '4'
    # 나머지가 0일때 몫은 십의자리가 한단계 낮춰서 계산해야함
    num_test1 = n // 3 # 0,0,1 / 1,1,2 / 2,2,3 / 3,3,4/
    num_test2 = n % 3 # 1,2,0 / 1,2,0 / 1,2,0 / 1,2,0
    if num_test2 == 0:
        answer = ((num_test1-1) * 10) + 4
    elif num_test2 == 2:
        answer = ((num_test1+1) * 10) + 2
    elif num_test2 == 1:
        answer = ((num_test1+1) * 10) + 1
    return str(answer)
print(solution(10)) 