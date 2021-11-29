# 고쳐야할것 : 처음부터 2차원배열로 만들고 시작해도 괜찮을듯
def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        arr_sum = []
        for j in range(len(arr1[0])):
            # arr_sum이라는 일차원 배열에 arr1과 arr2의 합을 넣음
            arr_sum.append(arr1[i][j] + arr2[i][j])
        # answer라는 일차원 배열에 arr_sum을 집어넣어 2차원 배열로 만듬
        answer.append(arr_sum)
    return answer