def selection_sort(array):
    array_copy = [*array]
    # Due to deep coupling in python, the algorithm erases the original array
    # For fix this using unpack array
    # immutable forever!
    result_array = []

    for i in range(len(array_copy)):
        current_min = min(array_copy)
        current_min_index = array_copy.index(current_min)
        this_min_selected = array_copy.pop(current_min_index)
        result_array.append(this_min_selected)

    return result_array
