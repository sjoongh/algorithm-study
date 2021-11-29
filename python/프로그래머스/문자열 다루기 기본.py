def solution(s):
    answer = True 
    s = list(s)
    if 4 == len(s) or len(s) == 6:
        answer = True
        for i in range(len(s)):
            # 아스키코드 값 i로
            i = ord(s[i])
            # 아스키코드 숫자 범위 내에 없다면 숫자가 아니므로
            # 계속 진행
            if ord('0') <= i <= ord('9'):
                continue
            else:
                answer = False
    else:
        answer = False
    return answer