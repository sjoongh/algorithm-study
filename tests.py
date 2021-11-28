n = int(input())
s = []
op = []
count = 1
tmp = True
for i in range(n):
    num = int(input())
    # count는 num과 같아질때까지
    while count <= num:
        # s에 count값 넣어줌
        s.append(count)
        # op는 나중에 출력 count가 올라갈때마다 +기호
        op.append('+')
        # count는 계속 증가
        count += 1
    # s의 마지막 값이 num과 같다면
    if s[-1] == num:
        # s의 마지막값 빼냄
        s.pop()
        # op는 -출력
        op.append('-')
    # stack의 마지막값이 x와 같아지지 않을경우
    else:
        tmp = False
if tmp == False:
    print('NO')
else:
    for i in op:
        print(i)


N, X = map(int, input().split(" ")) 
ARR = list(map(int, input().split(" ")))

N = int(input()) 
PAPER = [list(map(int, input().split(" "))) 
for i in range(N)]
