#   체육복

def solution(n, lost, reserve):
    # reserve 리스트에 있는 값이 lost 리스트에도 있으면 해당 값을 reserve 리스트에서 제거
    reserve_n = list(set(reserve) - set(lost))
    lost_n = list(set(lost) - set(reserve))

    answer = 전체 - 잃어버린 체육복 + 빌려준 체육복
    answer = n - len(lost_n)
    # lost_n의 list 요소를 for문으로 출력
    for i in lost_n:
        print(i)
        # i - 1의 값이 reserve_n에 있다면
        if i - 1 in reserve_n:
            # 체육복 하나를 빌려주고 reserve_n에서 그 값을 제외
            answer += 1
            reserve_n.remove(i - 1)
        # i + 1의 값이 reserve_n에 있다면
        elif i + 1 in reserve_n:
            # 체육복 하나를 빌려주고 reserve_n에서 해당값 제외
            answer += 1
            reserve_n.remove(i + 1)
    # return으로 count된 answer값을 출력함
    return answer
    # return n - len(lost_n) + answer로 해도됨