N = int(input())
li = []
for i in range(N):
    [x, y] = map(int, input().split())
    li.append([x, y])

li=sorted(li)
for j in range(len(li)):
    print(li[j][0], li[j][1])