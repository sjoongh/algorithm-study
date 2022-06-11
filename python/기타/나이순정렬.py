# 나이순 정렬
import sys

N = int(sys.stdin.readline())
people = []
for i in range(N):
    people.append(list(sys.stdin.readline().split()))
people.sort(key=lambda x: int(x[0]))
# people는 이중배열인 상태[age][name]이 들어가있음
# 위 람다식과 동일함 [1]로 하면 name으로 정렬됨
# def ladmbda(x):
    # return x[0]
for i in range(N):
    print(people[i][0], people[i][1])
