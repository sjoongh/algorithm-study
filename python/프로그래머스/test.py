def soultion(arr):
    answer = []
    for i in range(arr):
        if len(answer) == 0:
            answer.append(i)
        else:
            for j in range(answer):
                if j == i:
                    break
                else:
                    answer.append(i)
    return answer
