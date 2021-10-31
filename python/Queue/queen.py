# queen
# 인덱스가 행의 값이고 row[index]의 값이 열의 값이다.
def queen(x): # x와 i가 같으면 행이 같음, but for문을 보면 x와 i가 같을 수 없다
    for i in range(x): # 인덱스(i)가 행 row[n]값이 열
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i: # 열이 같거나 대각선이 같으면 false
            return False # 대각선이 같은 경우는 두 좌표에서 행 - 행 = 열 - 열이 같으면 두개는 같은 대각선상
    return True

# 한줄씩 재귀하며 dfs 실행
def dfs(x):
    # result를 전역으로 사용 하게함
    global result

    if x == N:
        result += 1
    # 각행에 퀸 놓기
    else:
        for i in range(N): # i는 열번호 0부터 N전까지 옮겨가며 유망한곳 찾음
            row[x] = i
            if queen(x): # 행,열,대각선 체크함수 true이면 백트래킹 안하고 계속 진행
                dfs(x + 1)

N = int(input())
# N크기만큼 행 만듬
row = [0] * N
result = 0
dfs(0)
print(result)