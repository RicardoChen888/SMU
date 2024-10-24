def min_changing(n):
    dp = [float("inf")] * (n + 1)

    dp[0] = 0

    coins = [1,3,4]
    for i in range(1, n+1):
        for coin in coins:
            if i>=coin:
                dp[i] = min(dp[i], dp[i-coin]+1)
    return dp[n]
money_value = 34
result = min_changing(money_value)
print(result)