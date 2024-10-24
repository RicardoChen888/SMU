def add_min_distance(s1, s2):
    n = len(s1)
    m = len(s2)

    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        dp[i][0] = i
    for j in range(1, n+1):
        dp[0][j] = j

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i][j-1]+1, dp[i-1][j]+1, dp[i-1][j-1]+1)
    return dp[m][n]


s1 = 'short'
s2 = 'ports'
times = add_min_distance(s1, s2)
print(f"times:{times}")