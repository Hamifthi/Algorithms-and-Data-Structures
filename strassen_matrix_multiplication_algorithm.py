import numpy as np

def matrix_multiplication_algorithm(array_a, array_b):
    def divide_matrix():
        # if array_a.shape == (2, 2):
        #     return array_a, array_b
        A1, A2 = np.split(array_a, 2, axis = 0)
        A11, A12 = np.split(A1, 2, axis = 1)
        A21, A22 = np.split(A2, 2, axis = 1)
        B1, B2 = np.split(array_b, 2, axis = 0)
        B11, B12 = np.split(B1, 2, axis = 1)
        B21, B22 = np.split(B2, 2, axis = 1)
        return A11, A12, A21, A22, B11, B12, B21, B22

a = np.arange(0, 4).reshape(2, 2)
b = np.arange(4, 8).reshape(2, 2)
sth = matrix_multiplication_algorithm(a, b)()
print(sth)