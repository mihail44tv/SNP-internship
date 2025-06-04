def is_palindrome(string):

    if isinstance(string, str):
        pass
    else:
        string = str(string)

    clean_string = ''

    for c in string:
        if ord(c) not in (32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 91, 92, 93, 94, 95, 96, 123,
                          124, 125, 126):
            clean_string += c.lower()

    return clean_string == clean_string[::-1]
