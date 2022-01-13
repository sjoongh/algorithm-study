#  문제를 작은문제로 나누어 푸는 문제

# n이 주어졌을 떄, n번째 피보나치 수를 구하는 프로그램

# 1. 재귀를 사용할 경우
def fibonacci(n):
    # n이 0과 1인 경우
    if n <= 1:
        # 그대로 n을 내보냄
        return n
    # 아닐 경우 재귀를 사용해 피보나치 수 리턴
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input())
print(fibonacci(n))


# 2. for문을 사용할 경우
n = int(input())
# fibonacci의 입력값이 0이나 1일 경우를 생각해 0,1을 넣고
# 두가지 수를 계속 더해줘야 하므로 0,1을 넣음
fibonacci = [0, 1]
# n까지 반복
for i in range(2, n+1):
    # [i-1]과 [i-2]의 자리의 값을 더함
    num = fibonacci[i-1] + fibonacci[i-2]
    # fibonacci 리스트에 추가
    fibonacci.append(num)
# 정답 인덱스만을 출력
print(fibonacci[n])