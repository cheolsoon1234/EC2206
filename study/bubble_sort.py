def bubble_sort(arr):

    for i in range(1, len(arr)):
        for j in range(0, len(arr)-i):
            if arr[j] > arr[j+1]:
                arr[j] ^= arr[j+1]
                arr[j+1] ^= arr[j]
                arr[j] ^= arr[j+1]

    return arr


print(bubble_sort([1, 3, 2, 5, 4, 5, 7, 5, 8, 8, 9, 1, 2]))