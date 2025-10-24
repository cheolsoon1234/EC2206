def ArrayAdditionI(arr):
    arr.sort()  # 굳이 정렬을 할 필요는 없지만 배열 내 최댓값을 편하게 가져오기 위해 사용함.
    s_min = 0
    s_max = 0

    for item in arr:
        if item < 0:
            s_min += item
        else:
            s_max += item

    offset = -s_min
    width = s_max - s_min
    target = arr[-1]
    arr.remove(target)  # 파이썬 그는 신인가
    dp = [False] * (width+1)

    dp[offset] = True

    for a in arr:
        if a >= 0:
            for s in range(width, -1, -1):
                ns = s + a
                if ns <= width and dp[s]:
                    dp[ns] = True
        else:
            for s in range(0, width + 1):
                ns = s + a
                if 0 <= ns and dp[s]:
                    dp[ns] = True

    if dp[target + offset]:
        return "true"
    else:
        return "false"


print(ArrayAdditionI(input()))
