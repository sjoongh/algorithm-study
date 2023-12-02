def solution(str_list, ex):
    text = ""
    for i in str_list:
        if ex not in i:
            text += i
    return text