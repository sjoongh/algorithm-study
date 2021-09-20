# 유클리드 호제법
# 즉 두 자연수 x,y에 대해 x를 y로 나눈 나머지를 r이라 하면(단 x > y), 
# x와 y의 최대공약수는 y와 r의 최대 공약수와 같음
# x,y의 최대공약수는 y,r의 최대 공약수와 같다는 원리
# r = x % y
# 즉 x에는 y값을 대입하고 y에는 (x % y)값인 r을 대입하다보면
# 언젠가는 x % y == 0 일때가 존재함
# x = 10, y = 12
# 10 % 12 == 12
# 12 % 10 == 2
# 10 % 2 == 0 --> 나머지값이 0일떄 y값 2가 최대공약수

# 방법 1
def solution(n, m):
    a = n
    b = m
    # 유클리드 호제법 기준에 맞추기위해 n > m보다 클경우 바꿔줌
    if n > m:
        n, m = m, n
    # m이 나눠질때까지 나누고 r에 m % n의 값을 넣음,
    # m에는 n값
    # n에는 r값
    while m % n:
        r = m % n
        m = n
        n = r
    # n값에는 최소공배수의 값이 들어있음
    return [n, a*b/n]

# GCD(최대공약수) --> GCD(B, A%B) if A%B = 0, GCD=B else GCD(B, A%B)
# LCM(최소공배수) --> (A*B) / GCD
# 방법2는 위의 방법을 재귀로 설정해 반복문을 안돌린 것
def gcd(n, m):
    mod = m % n
    if mod != 0:
        m, n = n, mod
        return gcd(n, m)
    else:
        return n

def solution(n, m):
    return [gcd(n, m), int(m*n / gcd(n, m))]