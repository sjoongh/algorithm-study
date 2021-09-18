def solution(arr):
    # range(len(arr))을 하면 range(0, 4)가 나옴 -> 0,1,2,3 반복
    # sum()값으로 전체 요소 합산 후 / arr의 개수 만큼 나눔 --> 평균값
    return sum([c for c in arr]) / len(arr)
print(solution([1,2,3,4]))