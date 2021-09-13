def solution(arr):
    # range(len(arr))을 하면 range(0, 4)가 나옴
    return sum([c for c in arr]) / len(arr)
print(solution([1,2,3,4]))