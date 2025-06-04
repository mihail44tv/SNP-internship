def connect_dicts(dict1, dict2):

    sum_d1 = sum(dict1.values())
    sum_d2 = sum(dict2.values())

    result_dict = dict()

    if sum_d1 > sum_d2:
        for key in dict2:
            if dict2[key] > 10:
                result_dict[key] = dict2[key]
        for key in dict1:
            if dict1[key] > 10:
                result_dict[key] = dict1[key]
    else:
        for key in dict1:
            if dict1[key] > 10:
                result_dict[key] = dict1[key]
        for key in dict2:
            if dict2[key] > 10:
                result_dict[key] = dict2[key]

    result_dict = dict(sorted(result_dict.items(), key=lambda item: item[1]))

    return result_dict
