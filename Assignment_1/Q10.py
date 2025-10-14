def CodelandUsernameValidation(strParam):

    if len(strParam) < 4 or len(strParam) > 25:
        return "false"

    if not strParam[0].isalpha():
        return "false"

    for ch in strParam:
        if not ch.isalnum():
            if not ch == '_':
                return "false"

    if strParam[-1] == '_':
        return "false"

    return "true"

print(CodelandUsernameValidation(input()))