import numpy as np
import random

def quick_select_algorithm(input_array, k_element):

    def partitioning(input_array, low, high):
        input_array_ = input_array[low:high]
        pivot = random.choice(input_array_)
        pivot_index = np.argwhere(input_array_ == pivot)[0][0]
        # print('pivot', pivot)
        input_array_[0], input_array_[pivot_index] = input_array_[pivot_index], input_array_[0]

        i = 1
        # print(low, '=====', high)
        for j in range(high - low):
            # print(input_array_)
            if input_array_[j] < pivot:
                input_array_[j], input_array_[i] = input_array_[i], input_array_[j]
                i += 1
            else:
                continue

        input_array_[0], input_array_[i - 1] = input_array_[i - 1], input_array_[0]
        pivot_index = np.argwhere(input_array == pivot)[0][0]
        return input_array, pivot_index, pivot

    def quick_select(input_array, low, high, k_element):
        input_array, pivot_index, pivot = partitioning(input_array, low, high)
        # print('pivot_index', pivot_index)
        # print('k_element', k_element)
        if k_element == pivot_index:
            return pivot

        elif k_element < pivot_index:
            return quick_select(input_array, low, pivot_index, k_element)

        elif k_element > pivot_index:
            return quick_select(input_array, pivot_index + 1, high, k_element)

    return quick_select(input_array, 0, len(input_array), k_element)

input_array = np.array(random.sample(range(10), 5))
print(input_array)
print(quick_select_algorithm(input_array, 2))