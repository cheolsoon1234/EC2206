def LetterCapitalize(strParam):

    capitalize_flag = 1
    result = ""

    for ch in strParam:
        if ch == ' ':
            capitalize_flag = 1
            result += ' '

        else:
            if capitalize_flag == 1:
                result += ch.upper()
            else:
                result += ch

            capitalize_flag = 0

    return result

print(LetterCapitalize(input()))