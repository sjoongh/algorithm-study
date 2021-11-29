def solution(n):
    answer = ''
    while n > 0:
        # 찾으려는 자리에서 -1을 해야 계산이 됨(배열은 0,1,2 순서이므로)
        n -= 1
        # 3진법으로 계산
        # 나머지는 0,1,2의 반복이므로
        # [n%3]으로 나눈 값이 0,1,2로 나오면
        # '124'중에 0 -> 1, 1 -> 2, 2 -> 4에 넣어줌
        # +answer를 통해 while문이 돌아갈때 전에 나왔던 answer값을 계속 붙여줌
        answer = '124'[n%3] + answer
        n //= 3
    return answer