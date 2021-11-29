def solution(s):
    answer = True
    p = s.count('p')
    P = s.count('P')
    y = s.count('y')
    Y = s.count('Y')
    if P+p == y+Y:
        return True
    elif p+P == y+Y == 0:
        return True
    else:
        return False