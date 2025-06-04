def coincidence(list=None, range=None):
    if list is None:
        list = []
    if range is None:
        range = []

    result = []

    for l in list:
        if l in range:
            result.append(l)
        elif isinstance(l, float):
            if int(l) in range:
                result.append(l)

    return result

