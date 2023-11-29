def solution(strArr):
    answer = []
    count = 0
    roop = 0
    while True:
        roop += 1
        for i in range(len(strArr)):
            if roop == len(strArr[i]):
                count += 1
        if count == 0:
            break
        answer.append(count)
    return max(answer)

print(solution(["a","bc","d","efg","hi"]))