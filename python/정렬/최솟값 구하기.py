# 첫 시도시 sort를 사용하면 시간복잡도가 올라갈 것 같아
# test = len(A)
# for i in range(test):
#     answer += min(A) * max(B)
#     A.remove(min(A))
#     B.remove(max(B))
# 위와 같은 식으로 A와 B의 요소를 줄여나갔는데
# sort로 정렬하고 for문 돌리는게 시간복잡도가 오히려 효율이 좋았다...
# min+max를 구하고 remove하는 것의 효율이 sort보다 떨어지는 듯

def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse = True)
    for i in range(len(A)):
        answer += A[i] * B[i]
    return answer