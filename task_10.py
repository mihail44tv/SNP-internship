def count_words(string):

    words = []
    word = ''

    for c in string + ' ':
        if c.isalpha():
            word += c.lower()
        elif not c.isalpha() and word != '':
            words.append(word)
            word = ''
        else:
            word = ''
    print(words)
    result = dict()

    for word in words:
        result[word] = words.count(word)

    return result
