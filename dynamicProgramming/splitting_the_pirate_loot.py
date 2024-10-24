def knapsack(nums):
    total_sum = sum(nums)

    if total_sum % 3 != 0:
        return 0

    target = total_sum // 3
    n = len(nums)

    dp = [[False] * (target + 1) for _ in range(target + 1)]

    dp[0][0] = True

    for num in nums:
        for j in range(target, num-1, -1):
            for k in range(target, num-1,-1):
                dp[j][k] = dp[j][k] or dp[j-num][k] or dp[j][k-num]

    return 1 if dp[-1][-1] else 0

n = 4
nums = [3,3,3,3]
print(knapsack(nums))
