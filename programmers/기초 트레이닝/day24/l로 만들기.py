def solution(myString):
    answer = ''
    for i in myString:
        if 'l' > i:
            answer += 'l'
        else:
            answer += i
    return answer