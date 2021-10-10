def solution(sizes):
    answer = 0
    change_sizes = []
    for i in sizes:
        if i[0] < i[1]:
            i[0], i[1] = i[1], i[0]
        change_sizes.append(i)
    width = [j[0] for j in change_sizes]
    height = [k[1] for k in change_sizes]
    answer = max(width) * max(height)
    return answer