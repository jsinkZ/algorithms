def bin_search(array, key, start, end):
    if end - start <= 1:
        if key < array[start]:
            return start - 1
        else:
            return start
    mid = (start + end) // 2
    if array[mid] < key:
        return bin_search(array, key, mid, end)
    elif array[mid] > key:
        return bin_search(array, key, start, mid)
    else:
        return mid
