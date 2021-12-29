import sys

N=int(sys.stdin.readline())
li=[]

for _ in range(N):
    li.append(list(map(int, sys.stdin.readline().split())))
for i in range(N):
    # y를 기준으로 정렬하기 위해 반대로 넣어줌
    li[i][0],li[i][1]=li[i][1],li[i][0]
# 오름차순 정렬
li.sort()
for i in range(N):
    # 출력된 값은 xy 순서이므로 다시 swap
    li[i][0],li[i][1]=li[i][1],li[i][0]
    print(li[i][0], li[i][1])