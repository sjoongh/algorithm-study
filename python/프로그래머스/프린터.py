def solution(priorities, location):
    answer = 0
    while True:
        # 가장 큰 수부터 출력
        max_num = max(priorities)
        for i in range(len(priorities)):
            # 가장 큰 수와 리스트의 요소가 일치한다면
            if max_num == priorities[i]:
                # 프린트
                answer += 1
                # 프린트 요소는 0
                priorities[i] = 0
                # 다시 max_num값을 구함(동일값이 존재할 수 있으므로)
                max_num = max(priorities)
                # location과 i의 값이 일치하면 answer반환
                if i == location:
                    return answer
print(solution([1, 1, 1, 1], 2))