def solution(num_list):
    answer = 0
    for i in num_list:
        while i != 1:
            if i % 2 == 0:
                answer += 1
                i = i // 2
            else:
                answer += 1
                i = (i - 1) // 2

    return answer