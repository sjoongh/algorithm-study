def solution(arr):
    answer = []
    count = 0
    for i in range(len(arr)):
        # i == 0일때부터 우선 첫번째값 넣어줌
        if i == 0:
            answer.append(arr[i])
        # 현재 요소와 바로 전 인덱스 요소 비교, 연속수가 아니라면?
        # 파이썬에서도 c와 같이 배열의 바로 전 인덱스 비교는 [i-1]로 가능
        # but [-1:]처럼 배열의 마지막요소를 확인하는 방법이 편할듯
        elif arr[i] != arr[i-1]:
            # append로 넣어줌
            answer.append(arr[i])
    return answer

print(solution([1,1,3,3,0,1,1]))

def no_continuous(s):
    # 빈 배열
    a = []
    # s반복문
    for i in s:
        # a배열의 a[-1] 마지막값이 [i]와 같다면
        # 없으면 연속수가 아니므로 append
        # 배열안의 요소의 값을 확인해야 하므로 [i]와 a[-1:]로 비교
        if a[-1:] == [i]:
            continue
        a.append(i)
    return a