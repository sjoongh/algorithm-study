# 나의 풀이
def solution(arr):
    answer = []
    for i in arr:
        answer += [i] * i
    return answer


# 풀어서 쓰면 for i in arr안에 for j in range(i) 를 넣어서 리스트에 i를 i번 넣게 한것
# 한줄 코딩.. 잘해서 구경해봤다
def solution(arr):
    return [i for i in arr for j in range(i)]