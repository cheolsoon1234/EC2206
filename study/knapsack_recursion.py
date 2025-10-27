def knapsack_recursion(n, m, p, w):
    p = [0] + p
    w = [0] + w

    dp = [[-1] * (m + 1) for _ in range(n + 1)]

    def solve(i, cap):
        if i == 0 or cap == 0:
            return 0
        if dp[i][cap] != -1:
            return dp[i][cap]

        if w[i] > cap:
            dp[i][cap] = solve(i - 1, cap)
            return dp[i][cap]

        dp[i][cap] = max(solve(i - 1, cap), solve(i - 1, cap - w[i]) + p[i])
        return dp[i][cap]

    return solve(n, m)


num_obj = 4
capacity = 8
profit = [1, 2, 5, 6]
weight = [2, 3, 4, 5]

print(knapsack_recursion(num_obj, capacity, profit, weight))
