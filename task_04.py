def sort_list(list):

    if not list:
        return list
    else:
        max_ = max(list)
        min_ = min(list)

        result = []

        for l in list:
            if l == max_:
                result.append(min_)
            elif l == min_:
                result.append(max_)
            else:
                result.append(l)

        result.append(min_)
        return result

