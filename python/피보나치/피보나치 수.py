# 방법1.
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


# 방법 2. 
# 재귀함수를 사용한 피보나치, 시간효율이 안 좋음
# def F(n):
#     if n < 2:
#         return n
#     else:
#         return F(n-1) + F(n-2)

# def solution(n):
#     answer = 0
#     for i in range(n):
#         answer = F(n)
#     answer %= 1234567
#     return answer


# 방법 3.
# 방법1보다는 직관적 방법
# def solution(n):
#     answer = []
#     for i in range(n+1):
#         if i==0 or i==1:
#             answer.append(i)
#         else:
#             f = answer[i-1] + answer[i-2]
#             answer.append(f % 1234567)

#     return answer[-1]