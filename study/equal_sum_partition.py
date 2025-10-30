def equal_sum_partition(arr):
    n = len(arr)
    s_min = s_max = 0
    for item in arr:
        if item >= 0:
            s_max += item
        else:
            s_min += item

    target = (s_max - s_min)

    if target % 2 == 1:  # 배열 전체의 합이 홀수이면 불가능
        return False

    target %= 2

    dp = [[-1] * (target+1) for _ in range(n+1)]

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

    if solve(n, target) == 1:
        return True
    else:
        return False


array = [1, 5, 11, 5]
print(equal_sum_partition(array))
