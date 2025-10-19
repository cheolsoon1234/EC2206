def insert_rec(sorted_list, value):
    if not sorted_list:
        return [value]
    if value <= sorted_list[0]:
        return [value] + sorted_list
    return [sorted_list[0]] + insert_rec(sorted_list[1:], value)


def SortArrayusingrecursion(arr):
    if not arr:
        return []
    if len(arr) == 1:
        return arr[:]

    last = arr[-1]
    sorted_rest = SortArrayusingrecursion(arr[:-1])

    return insert_rec(sorted_rest, last)


print(SortArrayusingrecursion(input()))
