def solution(my_string):
    answer = []
    my_list = my_string.split(" ")
    for i in my_list:
        if i != "":
            answer.append(i)
    return answer

print(solution(" i    love  you"))