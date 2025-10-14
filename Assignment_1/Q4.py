def LetterChanges(strParam):

    result = ""
    for ch in strParam:
        if ch.isalpha():
            lower = ch.lower()
            if lower == 'z':
                new_ch = 'a'
            else:
                new_ch = chr(ord(lower) + 1)

            if new_ch in 'aeiou':
                new_ch = new_ch.upper()

            result += new_ch

        else:
            result += ch

    return result

print(LetterChanges(input()))