# 이항계수
from math import factorial
N, K = map(int, input().split())
B = factorial(N) // (factorial(K) * factorial(N-K))
print(B)

import sys
N = int(sys.stdin.readline())
# 1. []로 배열하나 생성해놓음
people = []
for i in range(N):
    # 2. 1에서 만든 []안에 []를 넣어서 이중배열을 만들어줌
    people.append(list(sys.stdin.readline().split()))
    print(people)

people.sort(key=lambda x: int(x[0]))

for i in range(N):
    print(people[i][0], people[i][1])