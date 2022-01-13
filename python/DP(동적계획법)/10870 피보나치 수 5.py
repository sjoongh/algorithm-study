#  dp : 큰 문제를 작은문제로 나누어 푸는 문제

# n이 주어졌을 떄, n번째 피보나치 수를 구하는 프로그램

# 재귀를 사용할 경우
def fibonacci(n):
    # n이 0과 1인 경우
    if n <= 1:
        # 그대로 n을 내보냄
        return n
    # 아닐 경우 재귀를 사용해 피보나치 수 리턴
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input())
print(fibonacci(n))

