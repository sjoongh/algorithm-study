# K번째 수
def solution(array, commands):
    answer = []
    for i in commands:
        # [1,5,2,6,3] -> 문제에서 2~5번째는 5,2,6,3
        # 컴퓨터 상에서 index : 2~5는 2,6,3 이기 때문이다
        # i[0] -> array[2:5] -> 2,6,3
        # array[1:5] -> 5,2,6,3
        new_array = array[i[0]-1:i[1]]
        new_array.sort()
        # 위와 같은 맥락으로 new_array[i[2]-1] 을 해야함
        # 3 -> 2번째 인덱스, 1 -> 0번째 인덱스
        answer.append(new_array[i[2]-1])
        print(new_array[i[2]-1])
    return answer
print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
