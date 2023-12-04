def solution(arr, k):
    answer = []
    for i in arr:
        if k % 2 == 0:
            answer.append(k+i)
        else:
            answer.append(k*i)
    return answer