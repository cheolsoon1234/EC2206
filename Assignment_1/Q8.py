def NumberReverse(strParam):

    nums = strParam.split()
    nums.reverse()

    return " ".join(nums)

print(NumberReverse(input()))