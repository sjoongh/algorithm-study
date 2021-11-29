# 크레인 인형뽑기 게임, 터트려서 사라진 인형의 개수 구하기
def solution(board, moves):
    answer = 0
    moved = [0]  # 인덱스 에러 방지
    for i in moves:  # moves의 1,5,3,5,1,2,1,4가 i에 순서대로 대입
        i -= 1
        for j in range(len(board)):  # range는 정수로 반복해야 하므로 len으로 board요소의 길이를 잰 다음 range로 반복
            if board[j][i] != 0:  # board[j][i]의 값이 0이 아닐때 -> board
                moved.append(board[j][i])  # moved리스트로 해당 값을 옮기고
                board[j][i] = 0  # 0으로 만듬
                if moved[-1] == moved[-2]:  # 맨 뒤의 요소 2개가 같다면
                    moved.pop(-1)  # 같은 요소 제거
                    moved.pop(-1)
                    answer += 2  # 인형이 2개씩 없어지므로
                break  # 크레인으로 인형을 하나 옮기면 다음 moves로 넘어가야함
    return answer