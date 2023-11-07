def solution(arr, queries):
    answer = []
    for i in queries:
        test = []
        for j in range(i[0], i[1]+1):
            if i[2] < arr[j]:
                test.append(arr[j])
        if test != []:
            answer.append(min(test))
        else:
            answer.append(-1)
    return answer