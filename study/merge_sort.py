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
    if len(arr) == 1:
        return arr[:]

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


print(merge_sort( [5, 2, 9, 1, 5, 6] ))