def count_subset_sum(arr, t):

    """ tabulation
    n = len(A)
    dp = [[0] * (T+1) for _ in range(n+1)]

    dp[0][0] = 1

    for i in range(1, n+1):
        a = A[i-1]
        for s in range(0, T+1):
            dp[i][s] = dp[i-1][s]
            if s >= a:
                dp[i][s] += dp[i-1][s-a]
    print('\n'.join('\t'.join(map(str, r)) for r in dp))
    return dp[n][T]
    """

    n = len(arr)
    dp = [[-1] * (t+1) for _ in range(n+1)]

    def solve(i, j):
        if i == 0:
            dp[i][j] = 0
        if j == 0:
            dp[i][j] = 1
        if dp[i][j] != -1:
            return dp[i][j]

        res = solve(i - 1, j)
        if j >= arr[i - 1]:
            res += solve(i - 1, j - arr[i - 1])

        dp[i][j] = res
        return res

    return solve(n, t)


array = [1, 5, 11, 5]
target = 11
print(count_subset_sum(array, target))

