def solution(citations):
    answer = 0
    lengths = len(citations)
    # 정렬 정방향으로 진행하기 위해
    citations.sort()
    for i in range(len(citations)):
        # len -i를 통해 역순으로 hIndex찾음
        hIndex = lengths - i
        # hIndex는 역으로 진행중이므로 hIndex보다 작은 것은 위에 i가 제외시켜줌
        # 나머지 hIndex보다 크거나 같은 것들만 비교하면 됨
        if hIndex <= citations[i]:
            # 조건에 부합하면 정답
            answer = hIndex
            break
    return answer
