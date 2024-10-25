def eval_expr(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b


def min_and_max(i, j, min_dp, max_dp, ops):
    min_val = float('inf')
    max_val = float('-inf')

    for k in range(i, j):
        op = ops[k]
        a = eval_expr(max_dp[i][k], max_dp[k + 1][j], op)
        b = eval_expr(max_dp[i][k], min_dp[k + 1][j], op)
        c = eval_expr(min_dp[i][k], max_dp[k + 1][j], op)
        d = eval_expr(min_dp[i][k], min_dp[k + 1][j], op)

        min_val = min(min_val, a, b, c, d)
        max_val = max(max_val, a, b, c, d)

    return min_val, max_val


def maximize_expression(expression):
    digits = []
    ops = []

    # 分离操作数和运算符
    for i in range(len(expression)):
        if i % 2 == 0:
            digits.append(int(expression[i]))
        else:
            ops.append(expression[i])

    n = len(digits)
    min_dp = [[0] * n for _ in range(n)]
    max_dp = [[0] * n for _ in range(n)]

    # 初始化
    for i in range(n):
        min_dp[i][i] = digits[i]
        max_dp[i][i] = digits[i]

    # 动态规划求解
    for s in range(1, n):  # s 是子问题的长度
        for i in range(n - s):
            j = i + s
            min_dp[i][j], max_dp[i][j] = min_and_max(i, j, min_dp, max_dp, ops)

    return max_dp[0][n - 1]


# 示例使用
expression = "5-8+7*4-8+9"
print(maximize_expression(expression))  # 输出：200
