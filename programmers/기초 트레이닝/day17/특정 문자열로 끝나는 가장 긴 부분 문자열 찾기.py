def solution(myString, pat):
    answer = ''
    answer = myString[:myString.rfind(pat)] + pat
    return answer

print(solution("AbCdEFG", "dE"))