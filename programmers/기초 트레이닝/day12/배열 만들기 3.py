def solution(arr, intervals):
    answer = []
    for i in intervals:
        for j in arr[i[0]:i[1]+1]:
            answer.append(j)
    return answer