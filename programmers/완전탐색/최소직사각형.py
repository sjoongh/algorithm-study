def solution(sizes):
    result_list = []
    for i in sizes:
        # sizes의 세로 길이가 가로길이보다 크다면
        if i[0] < i[1]:
            # 위치 변경
            i[0], i[1] = i[1], i[0]
        # 값 추가
        result_list.append(i)
    width = [j[0] for j in result_list]
    column = [j[1] for j in result_list]

    result = max(width) * max(column)

    return result