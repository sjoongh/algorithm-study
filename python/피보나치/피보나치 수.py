def solution(n):
    answer = 0
    a,b = 0,1
    for i in range(n):
        # F(0)부터 시작하는 b로 피보나치의 과정을 넣고
        # a값에 최종결과값을 넣음
        a,b = b,a+b
    # n번째 수를 1234567로 나누어야함
    answer = a%1234567
    return answer