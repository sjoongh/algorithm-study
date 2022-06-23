def solution(arr):

    maxValue = 0
    length = int(len(arr))
    order = []
    result = []
    startIdx = 0

    # 수직선에서 두 점 사이의 maxValue구함
    for i in range(length):
        for j in range(length):
            if maxValue < arr[i][j]:
                maxValue = arr[i][j]
                startIdx = i
                endIdx = j

    dic = {}
    for i in range(length):
        dic[i] = arr[startIdx][i]
    dic = sorted(dic.items(), key=lambda x: x[1]) # 순서대로 오름차순 정렬
    for i in range(length):
        order.append(dic[i][0])
    result.append(order)
    result.append(list(reversed(order)))

    return result


