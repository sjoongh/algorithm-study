def solution(s):
    answer = ''
    answer = list(map(int, s.split(' ')))
    answer.sort()
    return str(answer[0])+' '+str(answer[-1])
