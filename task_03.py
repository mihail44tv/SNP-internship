def max_odd(array):

    odd = []

    for a in array:
        if isinstance(a, int):
            if a % 2 != 0:
                odd.append(a)
        elif isinstance(a, float) and a - int(a) == 0:
            if a % 2 != 0:
                odd.append(a)

    if not odd:
        return None
    else:
        return max(odd)
