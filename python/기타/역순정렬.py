x = list(map(int, input()))
while x[0] != 0:
    if (x == x[::-1]): # [::-1] 처음부터 끝까지 -1칸 간격으로(역순)
        print('yes')
    else:
        print('no')
    x = list(map(int, input()))
