def solution(board, h, w):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == board[h][w]:
                print(board[i][j])
                if (i == h-1 or i == h+1) and (j == w):
                    answer += 1
                if (j == w -1 or j == w + 1) and (i == h):
                    answer += 1
    return answer