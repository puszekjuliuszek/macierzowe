from Number import Number
import numpy as np

def BMU(A,B): # Binet Matrix Multiplication
    if len(A) == 2:
        return A@B
    n = len(A) // 2
    A_11, A_12, A_21, A_22 = A[:n, :n], A[:n, n:], A[n:, :n], A[n:, n:]
    B_11, B_12, B_21, B_22 = B[:n, :n], B[:n, n:], B[n:, :n], B[n:, n:]

    M0 = BMU(A_11, B_11)
    M1 = BMU(A_12, B_21)
    M2 = BMU(A_21, B_11)
    M3 = BMU(A_22, B_21)
    M4 = BMU(A_11, B_12)
    M5 = BMU(A_12, B_22)
    M6 = BMU(A_21, B_12)
    M7 = BMU(A_22, B_22)

    C = np.array([[[M0 + M1], [M4 + M5]],
                         [[M2 + M3], [M6 + M7]]], dtype=Number)

    return C

if __name__ == "__main__":
    A = np.array([[Number(5),Number(2)],[Number(1),Number(1)]], dtype=Number)
    B = np.array([[Number(1),Number(2)],[Number(1),Number(-3)]], dtype=Number)
    print(BMU(A,B))
    print(Number.ADD_counter)
    print(Number.MUL_counter)