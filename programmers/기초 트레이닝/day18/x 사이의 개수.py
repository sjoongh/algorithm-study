def solution(myString):
    answer = []
    count = 0
    for i in myString:
        if i == 'x':
            answer.append(count)
            count = 0
            continue
        else:
            count += 1
    answer.append(count)
    return answer

print(solution("oxooxoxxox"))