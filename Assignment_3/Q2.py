def WaveSorting(arr):

    n = len(arr)

    for i in range(n - 1):
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    n = len(arr)
    m = n // 2

    for i in range(n - m):
        if arr[i] >= arr[i + m]:
            return "false"
    return "true"


print(WaveSorting( input() ))