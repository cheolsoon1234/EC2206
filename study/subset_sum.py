def subset_sum(arr, t):
    n = len(arr)
    dp = [[-1] * (t+1) for _ in range(n+1)]

    def solve(i, j):
        if j == 0:
            return 1
        if i == 0:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]

        if arr[i-1] > j:
            dp[i][j] = solve(i - 1, j)
        else:
            dp[i][j] = solve(i - 1, j) or (solve(i - 1, j - arr[i-1]))

        return dp[i][j]

    if solve(n, t) == 1:
        return True
    else:
        return False


array = [1, 2, 3, 4, 5, 6, 7]
target = 11
print(subset_sum(array, target))
