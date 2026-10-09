def flatten(lst):
    flat_lst = []
    for item in lst:
        if isinstance(item, list):
            flat_lst.extend(flatten(item))
        else:
            flat_lst.append(item)
    return flat_lst


print(flatten([1, [2, [3,4], 5], 6]))
