def solution(arr):

    maxValue = 0
    length = int(len(arr))
    order = []
    result = []
    startIdx = 0
    for i in range(length):
        for j in range(length):
            if maxValue < arr[i][j]:
                maxValue = arr[i][j]
                startIdx = i
                endIdx = j

    dic = {}
    for i in range(length):
        dic[i] = arr[startIdx][i]
    dic = sorted(dic.items(), key=lambda x: x[1])
    for i in range(length):
        order.append(dic[i][0])
    result.append(order)
    result.append(list(reversed(order)))
    return result


