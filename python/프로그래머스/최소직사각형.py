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

# 최근 생각한 방법
# def solution(sizes):
#     answer = 1
#     for i in range(len(sizes)):
#         sizes[i].sorted(sizes[i])
#     row = []
#     col = []
#     for i in range(len(sizes)):
#         row.append(sizes[i][0])
#         col.append(sizes[i][1])
#     answer = max(col) * max(row)
#     return answer