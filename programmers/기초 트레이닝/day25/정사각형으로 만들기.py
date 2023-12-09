def solution(arr):
    max_len = max(len(arr), len(arr[0]))
    answer = [[0] * max_len for i in range(max_len)]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            answer[i][j] = arr[i][j]
    return answer