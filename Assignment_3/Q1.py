def SecondGreatLow(arr):
    l = len(arr)

    for i in range(l - 1):
        for j in range(0, l - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    uniq = []
    for x in arr:
        if not uniq or uniq[-1] != x:
            uniq.append(x)

    if len(uniq) == 1:
        return f"{uniq[0]} {uniq[0]}"
    elif len(uniq) == 2:
        return f"{uniq[1]} {uniq[0]}"
    else:
        return f"{uniq[1]} {uniq[-2]}"

print(SecondGreatLow([2,2,2,5,5,5,6]))
