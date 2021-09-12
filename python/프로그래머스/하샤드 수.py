def solution(x):
    # 파이썬에서 리스트는 str의 각 단어들을 하나하나의 요소로 구분해서 리스트로 만들어줌
    # int형에서 리스트는 안됨
    arr = list(str(x))
    sum_ = 0
    for i in range(len(arr)):
        # arr[i]의 각각의 요소를 sum에 더함
        sum_ += int(arr[i])
        if x % sum_ == 0:
            answer = True
        else:
            answer = False
    return answer

# 방법
# def solution(x):
#     return x % sum([int(c) for c in str(x)]) == 0