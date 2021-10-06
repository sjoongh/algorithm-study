def solution(absolutes, signs):
    for i in range(len(absolutes)):
        if signs[i] == False:
            absolutes[i] = int('-'+str(absolutes[i]))
    return sum(absolutes)