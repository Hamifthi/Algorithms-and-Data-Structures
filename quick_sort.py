import numpy as np
import random

def quick_sort_algorithm(input_array):
    def partitioning(input_array):
        input_array = np.array(input_array)
        pivot = random.choice(input_array)
        pivot_index = np.argwhere(input_array == pivot)[0][0]
        input_array[0], input_array[pivot_index] = input_array[pivot_index], input_array[0]
        i = 0
        high = len(input_array)
        for j in range(1, high):
            print(pivot, input_array[j])
            if input_array[j] < pivot:
                input_array[j], input_array[i] = input_array[i], input_array[j]
                i += 1
            else:
                continue
        pivot_index = np.argwhere(input_array == pivot)[0][0]
        input_array[pivot_index], input_array[i] = input_array[i], input_array[pivot_index]

    return partitioning(input_array)
    
        
input_array = random.sample(range(12), 12)
print(input_array)
print(quick_sort_algorithm(input_array))