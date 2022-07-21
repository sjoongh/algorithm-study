a = int(input())
for _ in range(a):
    b = list(input())
    sum = 0
    for i in b:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0: 
            # sum이 0보다 작을경우 열린괄호보다 닫힌괄호가 많으므로 괄호가 아님
            # NO를 바로 출력하고 중단시킴
            print('NO')
            break
    if sum > 0: # sum이 0보다 클 경우도 '(' 이 하나더 많으므로 NO
        print('NO')
    elif sum == 0: # sum이 0일때만 올바른 답
        print('YES')
