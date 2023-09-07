import itertools

# 에라토스테네스의 체 구현
def findNumber(num):
    isTrue = True
    if int(num) == 0:
        isTrue = False
    # 시간초과 때문에 소수 판별 알고리즘 사용
    # num의 최대 약수가 int(num ** 0.5)이하이기 때문에 사용 -> 제곱근으로 활용하기 위해서 **을 사용
    # +1은 자기 자신까지 검사하기 위함임
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            isTrue = False
            break
    return isTrue

def solution(numbers):
    num = list(map(str, numbers))
    num.sort()

    answer = 0
    num_list = []
    num_list2 = []
    for i in range(1, len(numbers)+1):
        num_list += list(itertools.permutations(num, i))
        for j in num_list:
            num_list2.append(int("".join(j)))

    for k in set(num_list2):
        if k < 2:
            continue
        check = True
        check = findNumber(k)
        if check:
            answer += 1
    return answer