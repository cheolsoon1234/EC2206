def StringPeriods(strParam):
    n = len(strParam)
    if n == 1:
        return "-1"

    def is_repeat(i, K, L):
        if i == n:
            return True

        if i+L <= n and strParam[i:i+L] == K:
            return is_repeat(i+L, K, L)

        return False

    def search(L):
        if L == 0:
            return "-1"

        if n % L == 0 and n // L > 1:
            K = strParam[:L]
            if is_repeat(0, K, L):
                return K

        return search(L-1)

    return search(n)


print(StringPeriods(input()))
