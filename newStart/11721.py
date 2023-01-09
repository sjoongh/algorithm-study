a = input()

# range(시작값, 종료값, step)
for b in range(0, len(a), 10): # 0부터 len(n)까지 10씩 끊어서 i를 입력
    print(b)
    print(a[b:b+10]) # a[시작값: 원하는종료값+1] -> 10개씩 출력