def solution(money):
    n = len(money)

    # 첫 번째 집 도둑질 O
    dp = [0] * n
    dp[0] = money[0]
    dp[1] = dp[0]
    for i in range(2, n-1):
        dp[i] = max(dp[i-1], dp[i-2]+money[i])
    answer = max(dp)

    # 첫 번째 집 도둑질 X, 마지막집 도둑질
    dp = [0] * n
    dp[1] = money[1]
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2]+money[i])

    if max(dp) > answer:
        answer = max(dp)
    return answer