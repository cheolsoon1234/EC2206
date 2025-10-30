def target_sum(arr, t):
    n = len(arr)
    total = sum(arr)

    if abs(t) > total:
        return False

    width = 2*(total + 1)
    offset = total
    dp = [[-1] * width for _ in range(n + 1)]

    def solve(i, j):
        if i == n:
            return 1 if j == t else 0

        idx = j + offset
        if dp[i][idx] != -1:
            return dp[i][idx]

        a = arr[i]
        # +a 선택, -a 선택
        plus = solve(i + 1, j + a)
        minus = solve(i + 1, j - a)

        dp[i][idx] = plus + minus

        return dp[i][idx]

    return solve(0, 0)


array = [1, 1, 1, 1, 1]
target = 5
print(target_sum(array, target))
