def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr.pop(i)
        j = i - 1
        while j >= 0 and arr[j] > key:
            j -= 1
        arr.insert(j + 1, key)
    return arr


print(insertion_sort([1, 4, 3, 2, 5, 1, 3, 1, 0]))
