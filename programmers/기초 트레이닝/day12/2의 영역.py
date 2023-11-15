def solution(arr):
    answer = []
    if arr.count(2) == 1:
        return 2
    elif arr.count(2) == 0:
        return -1
    else:
        print(arr.index(2))
        print(str(arr).rfind("2"))
    return answer

print(solution([1,2,1,4,5,2,9]))