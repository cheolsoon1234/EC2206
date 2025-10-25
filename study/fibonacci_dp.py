def fibonacci(n):
    dp[0] = 0
    dp[1] = 1

    if dp[n] != -1:
        return dp[n]
    else:
        dp[n] = fibonacci(n-1) + fibonacci(n-2)
        return dp[n]


dp = [-1] * 10000  # init dp array
print(fibonacci(int(input())))
