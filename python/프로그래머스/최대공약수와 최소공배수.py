def solution(n, m):
    answer = []
    x = 0
    for i in range(1, m+1):
        for j in range(1, i+1):
            if j * n == i * m:
                x = i * m
    for k in range(1, x+1):
        if n % k == m % k == 0:
            answer.append(k)
            break
    answer.append(x)
    return answer