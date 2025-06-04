def multiply_numbers(inputs=None):

    if inputs is None:
        return None

    string = str(inputs)
    numbers = []

    for c in string:
        if c.isdigit():
            numbers.append(int(c))

    if not numbers:
        return None
    else:
        result = 1
        for n in numbers:
            result *= n
        return result
