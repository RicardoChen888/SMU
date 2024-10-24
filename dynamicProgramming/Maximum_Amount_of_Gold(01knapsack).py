def knapsack(capacity, weight):
    n = len(weight)
    dp = [[0] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(capacity+1):
            if weight[i-1] <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i-1]]+weight[i-1])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][capacity]