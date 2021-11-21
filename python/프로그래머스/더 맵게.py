def solution(scoville, K):
    # 가장 low 숫자 + (두번째로 low한 숫자 * 2)
    # 반복문의 반복은 K이상이 될때까지 섞는다
    answer = 0
    ans_li = []
    scoville.sort()
    for i in range(len(scoville)):
        if scoville[i] < K:
            ans_li.append(scoville[i])
    for j in range(len(scoville)):
        if scoville[j] < K and scoville[j+1] < K:
            min_num = scoville.popleft()
            min_num2 = scoville.popleft()
    return answer