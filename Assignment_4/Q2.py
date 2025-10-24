def DynamicAdventure(arr):

    x = arr[0]
    blocks = arr[1:]

    NEG_INF = -10000 * 10000
    dp = [NEG_INF] * len(blocks)  # small enough number for dp
    dp[0] = blocks[0]

    for i in range(1, len(blocks)):
        best = NEG_INF
        for jumps in range(1, x+1):
            prev = i - jumps
            if prev < 0:
                continue  # 경계 체크
            if dp[prev] == NEG_INF:
                continue  # 도달 불가 상태는 스킵
            best = max(best, dp[prev] + blocks[i])
        dp[i] = best

    return dp[-1]


print(DynamicAdventure(input()))
