def longest_common_subseq(str1, str2):
    n = len(str1)
    m = len(str2)
    # dp array
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n][m]

A = [7, 2, 9, 3, 1, 5, 9, 4]
B = [2, 8, 1, 3, 9, 7]
print(longest_common_subseq(A, B))