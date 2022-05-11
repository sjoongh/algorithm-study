wh = [0 for i in range(101)]
wh[1] = 1
wh[2] = 1
wh[3] = 1
for i in range(0, 98):
    # i = 1일때, i번째 숫자와 i + 1번째 숫자를 더한 값을 i + 3번째에 놓게 된다.
    wh[i + 3] = wh[i] + wh[i + 1]
T = int(input())
for i in range(T):
    n = int(input())
    print(wh[n])