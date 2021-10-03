def solution(d, budget):
    answer = 0
    # 정렬을 통해 숫자를 크기순으로 나열
    # 금액이 적은 부서부터 지원
    d.sort()
    for i in range(len(d)):
        # budget보다 작다면
        if d[i] <= budget:
            # answer += 1을 함
            answer +=1
            # 금액은 빼줌
            budget -= d[i]
        else:
            break
    return answer
    # 금액이 큰 부서를 제외하고 찾기위해 정렬
    # d.sort()
    # budget이 sum(d)보다 커질때까지
    # while budget < sum(d):
    # 신청금액이 큰 부서를 제외함
    #     d.pop()
    # 남은부서 출력
    # return len(d)