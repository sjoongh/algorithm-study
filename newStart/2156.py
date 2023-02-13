n = int(input())
glasses = []
for j in range(n):
    glasses.append(int(input()))
dp = [0] * (n + 1)
for i in range(1, n + 1):
    if i == 1:
        dp[i] = glasses[i - 1]
    elif i == 2:
        dp[i] = glasses[i - 1] + glasses[i - 2]
    else:
        dp[i] = max(dp[i - 1], dp[i - 2] + glasses[i - 1], dp[i - 3] + glasses[i - 2] + glasses[i - 1])
print(dp[n])