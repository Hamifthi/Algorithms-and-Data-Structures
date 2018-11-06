import numpy as np

def matrix_multiplication_algorithm(array_a, array_b):
    def divide_matrix():
        # if array_a.shape == (2, 2):
        #     return array_a, array_b
        A1, A2 = np.split(array_a, 2, axis = 0)
        A, B = np.split(A1, 2, axis = 1)
        C, D = np.split(A2, 2, axis = 1)
        B1, B2 = np.split(array_b, 2, axis = 0)
        E, F = np.split(B1, 2, axis = 1)
        G, H = np.split(B2, 2, axis = 1)
        return A, B, C, D, E, F, G, H

    def seven_blocks_multiplication(A, B, C, D, E, F, G, H):
        P1 = A * (F - H)
        P2 = (A + B) * H
        P3 = (C + D) * E
        P4 = D * (G - E)
        P5 = (A + D) * (E + H)
        P6 = (B - D) * (G + H)
        P7 = (A - C) * (E + F)
        return P1, P2, P3, P4, P5, P6, P7

    def calculate_final_result(P1, P2, P3, P4, P5, P6, P7):
        F11 = P5 + P4 - P2 + P6
        F12 = P1 + P2
        F21 = P3 + P4
        F22 = P1 + P5 - P3 - P7
        return F11, F12, F21, F22










a = np.arange(0, 4).reshape(2, 2)
b = np.arange(4, 8).reshape(2, 2)
sth = matrix_multiplication_algorithm(a, b)()
print(sth)