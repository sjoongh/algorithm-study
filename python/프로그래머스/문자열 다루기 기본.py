def solution(s):
    answer = True 
    s = list(s)
    if 4 == len(s) or len(s) == 6:
        answer = True
        for i in range(len(s)):
            i = ord(s[i])
            if ord('0') <= i <= ord('9'):
                continue
            else:
                answer = False
    else:
        answer = False
    return answer