def solution(scoville, K):
    answer = 0
    while min(scoville) < K:
        scoville.sort()
        # 에러 처리
        try:
            if scoville[0] < K:
                scoville.insert(0, scoville.pop(0)+(scoville.pop(0) * 2))
        # 모든 음식을 k이상으로 만들 수 없는 경우 -1을 return
        except IndexError:
            return -1
        answer += 1
    return answer