def self_min(array):
    min = None

    if len(array) > 0:
        min = array[0]
        for i in array[1:]:
            if min > i:
                min = i
    return min
