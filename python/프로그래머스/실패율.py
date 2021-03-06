def solution(N, stages):
    dic = {}
    num = len(stages)
    
    for i in range(1, N+1):
        if num != 0: # 0명이 되면 그 이후 스테이지는 어차피 0임
            c = stages.count(i)
            dic[i] = c / num
            num -= c
        else: 
            dic[i] = 0
    return sorted(dic, key = lambda x: dic[x], reverse = True)