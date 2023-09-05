def solution(numbers):
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for j in range(1, len(numbers)+1):
        if len(numbers) > len(p1):
            p1 = p1 * j
        if len(numbers) > len(p2):
            p2 = p2 * j
        if len(numbers) > len(p3):
            p3 = p3 * j
    count1 = 0
    count2 = 0
    count3 = 0
    for i in range(len(numbers)):
        if p1[i] == numbers[i]:
            count1 += 1
        if p2[i] == numbers[i]:
            count2 += 1
        if p3[i] == numbers[i]:
            count3 += 1
    answer = []
    maxs = max(count1, count2, count3)
    if maxs == count1:
        answer.append(1)
    if maxs == count2:
        answer.append(2)
    if maxs == count3:
        answer.append(3)
    answer.sort()
    return answer