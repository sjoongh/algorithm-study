#     오름차순 정렬
#     answer.sort()

#     return answer

# solution([[0, 0, 0, 0, 0],
#           [0, 0, 1, 0, 3],
#           [0, 2, 5, 0, 1],
#           [4, 2, 4, 4, 2],
#           [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4])  # -> 이중 for문으로 순서대로 값이 존재하는지 찾아봄 moves에 해당하는 값이 존재하면
#  해당 배열의 값을 0으로 만들고 옮김 -> 반복하다가 -> 마지막 if문에서 요소 2개가 같을경우 지움 그리고 answer += 2
#  break가 없으면 같은 요소가 제거되었음에도 for j문이 계속 돌아가므로 오류가 발생 그러므로 break로 moves의 다음요소를 찾아야함
# 내적, a와b를 곱해서 각 요소들 sum한 값
def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += (a[i] * b[i])

    return answer
