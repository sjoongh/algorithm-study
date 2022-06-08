# x만큼 간격이 있는 n개의 숫자
def solution(x, n):
    result = []
    for i in range(1, n+1):
        result.appen(x*i)
    return result