def selection_sort(arr):
    n = len(arr)
    for i in range(0, n-1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


print(selection_sort([1, 5, 3, 2, 4, 1, 2, 2, 5, 6, 4]))
