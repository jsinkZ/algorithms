def merge(a, b):
    result_array = []
    i = j = 0  # pointers
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result_array.append(a[i])
            i += 1
        else:
            result_array.append(b[j])
            j += 1
    if i < len(a):
        result_array += a[i:]
    if j < len(b):
        result_array += b[j:]

    return result_array


def merge_sort(array):
    if len(array) == 1:
        return array
    middle = len(array) // 2
    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])

    return merge(left, right)
