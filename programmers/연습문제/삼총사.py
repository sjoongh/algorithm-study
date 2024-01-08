import itertools

# itertools.permutations : 순열을 구해줌, (A,B)와 (B,A)는 다른것이라고 판단
# itertools.combination : 조합을 구해줌, (A,B)와 (B,A)는 같은것으로 취급
def solution(number):
    answer = 0
    for i in list(itertools.combinations(number, 3)):
        if sum(i) == 0:
            answer += 1
    return answer