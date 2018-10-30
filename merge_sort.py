import numpy as np
import random

def merge_sort_algorithm(input_array):
    # step 1: divide input array recursively
    def merge_sort(input_array):
        
        n = len(input_array)
        if n == 1:
            return input_array
        
        mid = int(n / 2)
        list_one = input_array[:mid]
        list_two = input_array[mid:]
        
        list_one = merge_sort(list_one)
        list_two = merge_sort(list_two)
        

        return merge(list_one, list_two)

    # step two merge two list in sorted order
    def merge(list_one, list_two):
        final_list = []
        n1, n2 = len(list_one), len(list_two)
        i, j = 0, 0
        
        while (i < n1 and j < n2):
            if list_one[i] < list_two[j]:
                final_list.append(list_one[i])
                i += 1
            else:
                final_list.append(list_two[j])
                j += 1

        while i < n1:
            final_list.append(list_one[i])
            i += 1
        while j < n2:
            final_list.append(list_two[j])
            j += 1
            
        return final_list
    return merge_sort(input_array)

input = random.sample(range(4), 4)
print(input)
print(merge_sort_algorithm(input))