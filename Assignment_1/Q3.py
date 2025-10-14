def FirstReverse(strParam):

    chars = []

    for ch in strParam:
        chars.append(ch)

    reversed_str = ""

    for _ in range(len(chars)):
        reversed_str += chars.pop()

    return reversed_str

print(FirstReverse(input()))