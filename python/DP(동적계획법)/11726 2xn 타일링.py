# solution 1
n = int(input())

dp = [0] * 1001

if n <= 3:
    print(n)
else:
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    print(dp[i]% 10007)


# solution 2
T = int(input())

dp = [0] * 1001
dp[1] = 1
dp[2] = 2

for i in range(3, 1001):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n] % 10007)