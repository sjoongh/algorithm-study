def solution(k, m, score):
    score.sort(reverse=True)
    answer = 0
    count = 0
    test = []
    for i in range(len(score)):
        if count == m:
            count = 0
            answer += min(test) * m
            test = []
        test.append(score[i])
        count += 1
    if count >= m:
        answer += min(test) * count
    return answer