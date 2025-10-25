def fibonacci(n):
    if n == 1:
        return 1
    if n == 0:
        return 0

    if dp[n] != -1:
        return dp[n]
    else:
        dp[n] = fibonacci(n-1) + fibonacci(n-2)
        return dp[n]


dp = [-1] * 10000  # init dp array
print(fibonacci(int(input())))
