def solution(myString):
    # filter는 원래 (조건함수, 적용요소) 인데
    # 함수가 None이라면 , 기본 함수는 가정되는데 그것은 false가 제거된 제거된 모든 반복된 원소들이다.
    answer = list(filter(None, myString.split("x")))
    return answer

print(solution("dxccxbbbxaaaa"))