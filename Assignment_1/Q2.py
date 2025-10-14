def LongestWord(sen):

    word = ""
    words = []

    for ch in sen:
        if ch.isalnum():
            word += ch

        else:
            if word:
                words.append(word)
                word = ""

    if word:
        words.append(word)

    max_word = ""
    for word in words:
        if len(max_word) < len(word):
            max_word = word

    return max_word

print(LongestWord(input()))