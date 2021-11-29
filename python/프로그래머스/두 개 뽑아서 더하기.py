# 두 개 뽑아서 더하기
def solution(numbers):
    answer = []
    # 0,1,2,3
    for i in range(len(numbers)):
        # 1,2,3
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i]+numbers[j])
    answer = list(set(answer))
    answer.sort()
    return answer

print(solution([5, 0, 2, 7]))
