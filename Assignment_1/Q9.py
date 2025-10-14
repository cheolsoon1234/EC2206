def HappyNumbers(num):

    num = int(num)

    seen = set()

    while num != 1 and num not in seen:
        seen.add(num)
        num = sum((int(digit) ** 2) for digit in str(num))

    if num == 1:
        return "true"
    else:
        return "false"

print(HappyNumbers(input()))