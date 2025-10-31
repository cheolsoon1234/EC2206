def num_of_subset_by_given_diff(arr, t):
    n = len(arr)
    total = sum(arr)

    if abs(t) > total:
        return False

    width = 2 * (total + 1)
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

    # print('\n'.join('\t'.join(map(str, r)) for r in dp))


array = [1, 2, 3, 4, 5]
target = 3
print(num_of_subset_by_given_diff(array, target))


# number of subsets by given difference 문제는 target sum 문제와 동일한 문제임
# target sum 문제는 -1/1 knapsack 문제
# number of subsets by given difference도 -1/1 knapsack 문제이고
# target을 difference로 잡으면 되는 이유도 -1/1 knapsack 문제이기 때문에 diff + 원소를 할 경우 동일한 원소 혹은 0이 존재하지 않으면 diff를 만족할 수 없기 때문이다.
# 그럼 target 을 만족하는 부분 집합 중에 동일한 원소가 2개 이상 있거나, 0이 존재하면 중복 조합을 계산한 후 곱해줘야  한다.



