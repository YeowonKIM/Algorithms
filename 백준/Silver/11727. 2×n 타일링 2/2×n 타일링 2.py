def tiling2(n):
    dp = [0] * 10001
    dp[0], dp[1] = 1, 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + 2 * dp[i-2]
    return dp[n]

n = int(input())
print(tiling2(n) % 10007)