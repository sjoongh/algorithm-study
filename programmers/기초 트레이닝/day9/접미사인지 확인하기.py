def solution(my_string, is_suffix):
    list_string = []
    answer = 0
    for i in range(1, len(my_string)+1):
        list_string.append(my_string[-i:])
        if my_string[-i:] == is_suffix:
            return 1
    return 0