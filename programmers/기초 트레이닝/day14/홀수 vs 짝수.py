def solution(num_list):
    answer = 0
    r = 0
    l = 0
    for i in range(len(num_list)):
        if i % 2 == 0:
            r += num_list[i]
        else:
            l += num_list[i]
    answer = max(r, l)
    return answer