# 계단 오르는 데는 다음과 같은 규칙이 있다.
# 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
# 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
# 마지막 도착 계단은 반드시 밟아야 한다.
# 따라서 첫 번째 계단을 밟고 이어 두 번째 계단이나, 세 번째 계단으로 오를 수 있다. 하지만, 첫 번째 계단을 밟고 이어 네 번째 계단으로 올라가거나, 첫 번째, 두 번째, 세 번째 계단을 연속해서 모두 밟을 수는 없다.
# 각 계단에 쓰여 있는 점수가 주어질 때 이 게임에서 얻을 수 있는 총 점수의 최댓값을 구하는 프로그램을 작성하시오.
# 입력
# 입력의 첫째 줄에 계단의 개수가 주어진다.
# 둘째 줄부터 한 줄에 하나씩 제일 아래에 놓인 계단부터 순서대로 각 계단에 쓰여 있는 점수가 주어진다. 계단의 개수는 300이하의 자연수이고, 계단에 쓰여 있는 점수는 10,000이하의 자연수이다.

# import sys

# num = int(sys.stdin.readline())

# s = [0 for i in range(301)] # 300이하의 자연수 이므로 300까지 돌림
# dp = [0 for i in range(301)]

# for i in range(num):
#     s[i] = int(input()) # state
# dp[0] = s[0] # start value
# dp[1] = s[0] + s[1] # first floor
# dp[2] = max(s[1] + s[2], s[0] + s[2]) # second floor
# # --> 계단을 올라가면서 max 값 dp저장
# for i in range(3, num):
#     # 2칸 이상 올라가면 안되므로 dp[i-3], dp[i-2] 비교
#     dp[i] = max(dp[i-3] + s[i-1] + s[i], dp[i-2] + s[i]) # start value + s[first value], second value + s[now value]
# print(dp[num-1])


import sys

num = int(sys.stdin.readline())

s = [0 for i in range(301)]
dp = [0 for i in range(301)]

for i in range(num):
    dp[0] = s[0]
    dp[1] = s[0] + s[1]
    dp[2] = max(s[1]+s[2], s[0]+s[2])

for i in range(num):
    dp[i] = max(dp[i-3]+s[i]+s[i-1], dp[i-2]+s[i])
print(dp[num-1])z