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


def bin_insertion_sort(array):
    for i in range(1, len(array)):
        temp = array[i]
        pos = bin_search(array, temp, 0, i) + 1

        for k in range(i, pos, -1):
            array[k] = array[k - 1]

        array[pos] = temp
    return array
