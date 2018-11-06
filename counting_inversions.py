from merge_sort import merge_sort_algorithm
import random

def counting_inversions_algorithm(input_array):
    n = len(input_array)
    middle = n / 2
    a = input_array[:int(middle)]
    b = input_array[int(middle):]

    a = merge_sort_algorithm(a)
    b = merge_sort_algorithm(b)

    c = []
    i, j, inversions = 0, 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1

        else:
            c.append(b[j])
            j += 1
            inversions += len(a[i:])

    while i < len(a):
        c.append(a[i])
        i += 1
    while j < len(b):
        c.append(b[j])
        j += 1

    return c, inversions

input_array = [1, 3, 5, 2, 4, 6]
print(input_array)
print(counting_inversions_algorithm(input_array))