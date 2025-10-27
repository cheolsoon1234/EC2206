def knapsack(n, m, p, w):
    p = [0] + p
    w = [0] + w

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for cap in range(1, m + 1):
            if w[i] <= cap:
                # change dp[i][cap] = max(dp[i-1][cap], dp[i-1][cap - w[i]] + p[i]) to dp[i][cap] = max(dp[i-1][cap], dp[i][cap - w[i]] + p[i])
                dp[i][cap] = max(dp[i-1][cap], dp[i][cap - w[i]] + p[i])
            else:
                dp[i][cap] = dp[i - 1][cap]

    return dp[n][m]


num_obj = 4
capacity = 8
profit = [1, 2, 5, 6]
weight = [2, 3, 4, 5]

print(knapsack(num_obj, capacity, profit, weight))
