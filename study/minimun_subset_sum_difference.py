def minimum_subset_sum_diff(arr):
    n = len(arr)
    total = sum(arr)
    half = total // 2

    # dp[i][s] = 앞에서 i개로 합 s를 만들 수 있으면 1(True), 아니면 0(False), None=미계산
    dp = [[None] * (half + 1) for _ in range(n + 1)]

    def solve(i, j):
        if j == 0:
            return 1
        if i == 0:
            return 0
        if dp[i][j] is not None:
            return dp[i][j]

        res = solve(i - 1, j)
        if res == 0 and j >= arr[i - 1]:
            res = solve(i - 1, j - arr[i - 1])
        dp[i][j] = res
        return res

    # half..0 중 가능한 가장 큰 s를 찾는다 -> 나머지 조건은 자동으로 따라옴.
    best_s = 0
    for s in range(half, -1, -1):
        if solve(n, s) == 1:
            best_s = s
            break

    return total - 2 * best_s


print(minimum_subset_sum_diff([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(minimum_subset_sum_diff([1, 1, 2, 5]))
