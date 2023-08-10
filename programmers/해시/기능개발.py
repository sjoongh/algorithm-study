def solution(progresses, speeds):

    answer = []
    time = 0
    count = 0

    while len(progresses)> 0:
        # 2. 100이 되면 pop으로 빼주고 count += 1
        # 3. 다음 수행 하는것도 100이라면 count+=1
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        # 4. 다음 수행 값이 100이 아니라면 answer에 넣어줌
        else:
            if count > 0:
                answer.append(count)
                count = 0
            # 1. 100이 될때까지 time을 늘림
            # 5. 다음 수행값 time시작
            time += 1
    answer.append(count)
    return answer