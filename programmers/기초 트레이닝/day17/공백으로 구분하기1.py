def solution(my_string):
    answer = []
    list_my = my_string.split(" ")
    for i in list_my:
        answer.append(i)
    return answer

print(solution("i love you"))