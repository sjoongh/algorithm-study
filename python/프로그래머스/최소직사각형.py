def solution(sizes):
    answer = 0
    x = []
    y = []
    x_num = 0
    y_num = 0
    for i in range(len(sizes)):
        x.append(sizes[i][0])
        y.append(sizes[i][1])
    x_num = max(x)
    y_num = max(y)
    for j in range(len(sizes)):
        if x_num < sizes[i][1]:
          x_num = sizes[i][0]
        elif y_num < sizes[i][0]:
            y_num = sizes[i][1]
    answer = x_num * y_num
    return answer