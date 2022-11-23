import time
import random

# config constants
NUMBER_OF_ELEMENTS = 1 * 10**4
MAX_RAND = 10**4


def generate_list(N, MAX_RAND):
    array = [0] * N
    for i in range(N):
        array[i] = random.randint(-MAX_RAND, MAX_RAND)
    return array


def test(algorithm, array=generate_list(NUMBER_OF_ELEMENTS, MAX_RAND)):
    success = False  # algorithm works correctly
    start_time = time.time()
    new_array = algorithm(array)  # new array by algorithm
    end_time = time.time()
    if new_array[-1] == max(array):
        success = True

    return "Time: " + str(end_time - start_time) + " Success: " + str(success)
