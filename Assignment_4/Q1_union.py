def ArrayAdditionI(arr):
    arr = sorted(arr)
    target = arr.pop()
    reach = {0}
    for a in arr:
        reach |= {s + a for s in reach}
    return "true" if target in reach else "false"


print(ArrayAdditionI([4, 6, 23, 10, 1, 3]))
