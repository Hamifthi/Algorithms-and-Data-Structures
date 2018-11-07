import numpy as np

def matrix_multiplication_algorithm(array_a, array_b):
    def divide_matrix(array_a, array_b):
        # cut input arrays in 4 parts and initiate 8 different values
        A1, A2 = np.split(array_a, 2, axis = 0)
        A, B = np.split(A1, 2, axis = 1)
        C, D = np.split(A2, 2, axis = 1)
        B1, B2 = np.split(array_b, 2, axis = 0)
        E, F = np.split(B1, 2, axis = 1)
        G, H = np.split(B2, 2, axis = 1)
        # check if the arrays are 2 by 2 and return final output here
        if array_a.shape == (2, 2):
            F11, F12, F21, F22 = calculation(A, B, C, D, E, F, G, H)
            return final_array_result(F11, F12, F21, F22)

        # this is the recursion part
        part1 = divide_matrix(A, E)
        part2 = divide_matrix(B, F)
        part3 = divide_matrix(C, G)
        part4 = divide_matrix(D, H)
        
        # return final calculated array
        return final_array_result(part1, part2, part3, part4)

    def calculation(A, B, C, D, E, F, G, H):
        # calculating septet P values here
        P1 = A * (F - H)
        P2 = (A + B) * H
        P3 = (C + D) * E
        P4 = D * (G - E)
        P5 = (A + D) * (E + H)
        P6 = (B - D) * (G + H)
        P7 = (A - C) * (E + F)
        # 4 parts of final array calculated here
        F11 = P5 + P4 - P2 + P6
        F12 = P1 + P2
        F21 = P3 + P4
        F22 = P1 + P5 - P3 - P7
        # now we return the 4 parts of final output array
        return F11, F12, F21, F22

    # assembling final output here
    def final_array_result(F11, F12, F21, F22):
        # calculating output array dimensions here
        n = 2 * F11.shape[0]
        # return final array here
        return np.array([F11, F12, F21, F22]).reshape(n, n)

    return divide_matrix(array_a, array_b)

a = np.arange(0, 16).reshape(4, 4)
b = np.arange(16, 32).reshape(4, 4)
sth = matrix_multiplication_algorithm(a, b)
print(sth)