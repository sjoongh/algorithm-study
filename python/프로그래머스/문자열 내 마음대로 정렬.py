# strings[n]번째 요소를 기존 strings맨 앞에 붙임 
# 배열의 i번째 맨 앞에 n(strings[i][n]) + 각 인덱스의 기존문자열(strings[i])
# strings를 정렬 후 [1:]부터 출력함
def solution(strings, n):
    answer = []
    for i in range(len(strings)):
        strings[i] = strings[i][n]+strings[i]

    strings.sort()
    
    for j in range(len(strings)):
        # 앞에 넣었던 n을 제외하기위해 인덱스1부터 다시 넣어줌
        answer.append(strings[j][1:])

    return answer

# 방법2. lambda사용
def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))