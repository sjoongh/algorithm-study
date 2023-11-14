def solution(q, r, code):
    answer = ''
    list_code = list(code)
    for i in range(len(list_code)):
        if i % q == r:
            answer += list_code[i]
    return answer