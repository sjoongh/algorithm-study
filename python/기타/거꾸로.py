# 거꾸로 별찍기
n = int(input())

for i in range(1, n+1):
   print(" "*(n-i) + "*" * i)

N, X = map(int, input().split())
A = list(map(int,input().split())) -> 리스트(한줄)에 입력 할 수 있는 빈 리스트
a=[] -> 빈 리스트 생성

for i in A:
   if i < X:
       a.append(i) -> append(i)로 빈리스트에 i값 넣어줌
for i in a:
   print(i, end=' ') -> 리스트에 담긴 값 출력

