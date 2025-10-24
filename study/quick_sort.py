def partition(arr, l, h):
    pivot = arr[l]
    i = l + 1
    j = h

    while i <= j:
        while i <= h and arr[i] <= pivot:
            i += 1
        while j >= l + 1 and arr[j] > pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    arr[l], arr[j] = arr[j], arr[l]
    return j


def quicksort(arr, l, h):
    if l < h:
        p = partition(arr, l, h)
        quicksort(arr, l, p - 1)
        quicksort(arr, p + 1, h)
    return arr


array = [1, 5, 4, 3, 2, 1, 6, 7, 8, 8, 5, 9, 0, -1, -2, -10, -1, 0, 10, 11]
print(quicksort(array, 0, len(array)-1))
