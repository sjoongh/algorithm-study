def solution(myStr):
    answer = []
    text = ""
    for i in myStr:
        if i != "a" and i != "b" and i != "c":
            text += i
        elif len(text) != 0:
            answer.append(text)
            text = ""
    if len(text) != 0:
        answer.append(text)
    return ["EMPTY"] if len(answer) == 0 else answer

print(solution("baconlettucetomato"))