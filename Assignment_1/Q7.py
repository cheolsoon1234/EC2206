def ConsonantCount(strParam):

    count = 0
    for ch in strParam:
        if ch.lower() in "bcdfghjklmnpqrstvwxyz":
            count += 1

    return count

print(ConsonantCount(input()))