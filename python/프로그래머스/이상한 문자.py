def solution(s):
    answer = ''
    s_list = list(str(s))
    
    for i in range(len(s_list)):
        if i % 2 == 0:
            s_list[i] = s_list[i].upper()
        elif i % 2 == 1:
            s_list[i] = s_list[i].lower()
    s="",join(s_list)
    answer = " ".join(s)
    return answer