import math

def solution(n):
    # 0과 1을 제외시킬거임 밑에서 && +1의 이유는 n자리까지 넣어주기 위함
    n_list = [True] * (n+1)
    answer = 0
    # sqrt는 제곱근을 구하는 함수 --> n의 제곱근 값까지만 검사하면 됨
    # i == sqrt(n)까지 검사하기 위해 + 1을 더해준다
    for i in range(2, int(math.sqrt(n))+1):
        if n_list[i] == False:
            continue
        # n_list의 값이 소수라면 False로 만듬
        for j in range(i+i, n+1, i):
            n_list[j] = False
    # n_list초기값 선언 시 0과 1에 대한 예외처리를 하지 않았으므로
    # 2부터 시작하여 제외시킴, +1은 n까지 검사하기 위함
    for i in range(2, n+1):
        # True인 값만 += 1
        print(i)
        if n_list[i] == True:
            answer += 1
    return answer

print(solution(10))