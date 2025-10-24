def merge(left, right):
    i = 0
    j = 0
    out = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i])
            i += 1
        else:
            out.append(right[j])
            j += 1

    if i < len(left):
        out.extend(left[i:])
    if j < len(right):
        out.extend(right[j:])

    return out


def merge_sort(arr):
    n = len(arr)
    width = 1
    while width < n:
        new_arr = []
        for start in range(0, n, 2 * width):
            mid = min(start + width, n)
            end = min(start + 2 * width, n)

            if mid < end:
                new_arr.extend(merge(arr[start:mid], arr[mid:end]))
            else:
                new_arr.extend(arr[start:mid])
        width *= 2
        arr = new_arr
    return arr


print(merge_sort([1,2,1,9,3,2,65,4,2,76,23,26,2,6,1,9]))