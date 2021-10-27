def solution(numbers):
    answer = ''
    test = ''
    # 조건 1. 앞자리 num이 높은게 출력
    # 조건 2. 9가 쓰이려면 99, 98
    # 방법1. numbers를 하나씩 쪼개서 계산
    for i in numbers:
        test += str(i)