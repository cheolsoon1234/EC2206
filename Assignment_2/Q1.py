def RemoveBrackets(strParam):
    opened = 0
    for ch in strParam:
        if ch == '(':
            opened += 1
        elif ch == ')':
            if opened > 0:
                opened -= 1
            else:
                opened += 1

    return opened

print(RemoveBrackets(input()))