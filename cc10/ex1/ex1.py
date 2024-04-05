import sys
if sys.version_info[0] == 3:
    from functools import reduce
else:
    pass

def map_function(data):
    return [(0, value) for value in data]

def reduce_function_min(key, values):
    return min(values)

def reduce_function_max(key, values):
    return max(values)

def map_group(data):
    mapped_data = map_function(data)
    grouped_data = sorted(mapped_data, key=lambda x: x[0])
    return grouped_data

def min(data):
    grouped_data = map_group(data)
    return reduce(reduce_function_min, grouped_data)

def max(data):
    grouped_data = map_group(data)
    return reduce(reduce_function_max, grouped_data)