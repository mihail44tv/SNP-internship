def combine_anagrams(words_array):

    keys = []

    for word in words_array:
        keys.append("".join(sorted(word.lower())))

    dict_ = dict()

    for key in keys:
        if dict_.get(key) is None:
            dict_[key] = []

    for word in words_array:
        dict_["".join(sorted(word.lower()))].append(word)

    result = []

    for value in dict_.values():
        result.append(value)

    return result
