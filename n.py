def flatten_list(nested_list):
    flate = []
    for item in nested_list:
        if isinstance(item,list):
            flate.extend(flatten_list(item))
        else:
            flate.append(item)
    return flate

print(flatten_list([1, [2, [3, 4]], 5]))