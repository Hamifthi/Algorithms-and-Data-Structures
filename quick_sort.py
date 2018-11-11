import numpy as np
import random

def quick_sort_algorithm(input_array):

    def partitioning(input_array, low, high):
        pivot = random.choice(input_array[low:high])
        pivot_index = np.argwhere(input_array == pivot)[0][0]
        input_array[low], input_array[pivot_index] = input_array[pivot_index], input_array[low]

        i = low + 1
        for j in range(low, high):
            if input_array[j] < pivot:
                input_array[j], input_array[i] = input_array[i], input_array[j]
                i += 1
            else:
                continue

        input_array[low], input_array[i - 1] = input_array[i - 1], input_array[low]
        pivot_index = np.argwhere(input_array == pivot)[0][0]
        return input_array, pivot_index

    def quick_sort(input_array, low, high):

        if high > low:

            input_array, pivot_index = partitioning(input_array, low, high)

            quick_sort(input_array, low, pivot_index)
            quick_sort(input_array, pivot_index + 1, high)
        
    return quick_sort(input_array, 0, len(input_array))
    
        
input_array = np.array(random.sample(range(15), 15))
print(input_array)
print(quick_sort_algorithm(input_array))
print(input_array)