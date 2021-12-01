def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        skill_li = list(skill)
        for j in i:
            # BACDE
            if j in skill:
                # skill_li의 순서대로 진행되어야 하므로
                # 앞글자부터 pop으로 뺄 때 순서가 맞지 않는다면
                # 틀렸으므로 break, 아닐경우는 answer += 1
                if j != skill_li.pop(0):
                    break
        # for-else문, break에 걸리지 않고 for문을 나오면 else문으로 들어옴
        else:
            answer += 1
    return answer