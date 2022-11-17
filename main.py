import time
import random

# config

NUMBER_OF_ELEMENTS = 4 * 10**4
MAX_RAND = 10**4

# system testing functions

def generate_list(N, MAX_RAND):
    l = [0] * N
    for i in range(N):
        l[i] = random.randint(-MAX_RAND, MAX_RAND)
    return l

def test(alg, r):
    s = time.time()
    a = alg(r)
    e = time.time()
    if (a[-1] == max(a)): print(e - s, True)
    else:
        print(e - s, False)

# min/max sorting alg

def mn(a):
    min = None
    if len(a) > 0:
        min = a[0]
        for i in a[1:]:
            if min > i:
                min = i
    return min
    l = [0] * N
    for i in range(N):
        l[i] = random.randint(-MAX_RAND, MAX_RAND)
    return l

# sorting alg

def bubble_sort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

def selection_sort(a):
    r = []
    
    for i in range(len(a)):
        m = min(a)
        j = a.index(m)
        n = a.pop(j)
        r.append(n)
    
    return r

def insertion_sort(a):
    for i in range(1, len(a)):
        k = a[i]
        j = i - 1
        while j >= 0 and a[j] > k:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = k

    return a


    for i in xrange(1, len(arr)):
        val = arr[i]
        j = binary_search(arr, val, 0, i-1)
        arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]
    return arr

def binary_insertion_sort(a):
    for i in range(1, len(a)):
        temp = a[i]
        pos = binary_search(a, temp, 0, i) + 1
        for k in range(i, pos, -1):
            a[k] = a[k - 1]
        a[pos] = temp
    return a
 
def binary_search(a, key, start, end):
    if end - start <= 1:
        if key < a[start]:
            return start - 1
        else:
            return start
    mid = (start + end)//2
    if a[mid] < key:
        return binary_search(a, key, mid, end)
    elif a[mid] > key:
        return binary_search(a, key, start, mid)
    else:
        return mid

# setup and test alg

a = generate_list(NUMBER_OF_ELEMENTS, MAX_RAND)
test(bubble_sort, a) # ~ 42 sec
a = generate_list(NUMBER_OF_ELEMENTS, MAX_RAND)
test(selection_sort, a) # ~ 12 sec
a = generate_list(NUMBER_OF_ELEMENTS, MAX_RAND)
test(insertion_sort, a) # ~ 37 sec
a = generate_list(NUMBER_OF_ELEMENTS, MAX_RAND)
test(binary_insertion_sort, a) # ~ 17 sec

