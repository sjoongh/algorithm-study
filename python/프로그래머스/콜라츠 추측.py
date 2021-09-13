def solution(num):
    answer = 0
    for i in range(500):
        if num == 1:
            break
        if i == 499 and num != 1:
            answer = -1
            break
        if num % 2 == 0:
            answer += 1
            num = num // 2
        else:
            answer += 1
            num = (num * 3) + 1
    return answer