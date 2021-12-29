import sys

N = int(sys.stdin.readline())
li = []

for i in range(N):
    [x, y] = map(int, input().split())
    li.append([x, y])
# 정렬
li=sorted(li)
for j in range(len(li)):
    # x좌표 기준이므로 그대로 출력
    print(li[j][0], li[j][1])