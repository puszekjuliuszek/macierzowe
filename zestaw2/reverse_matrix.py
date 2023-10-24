from Strassen import SMU as mul
from Number import Number
import numpy as np


def reverse_matrix(A) -> np.array:
    n = len(A)
    if n == 1:
        a = A[0][0]
        if a != 0:
            return np.array([[1/a]], dtype=Number)
        else:
            raise ValueError("Matrix is not invertilbe")
    n//=2
    A_11, A_12, A_21, A_22 = A[:n,:n], A[:n,n:], A[n:,:n],A[n:,n:]
    invA_11 = reverse_matrix(A_11)
    S = A_22 - mul(mul(A_21, invA_11),A_12) 
    invS = reverse_matrix(S)
    C = np.zeros((2*n,2*n), dtype=Number)
    C[:n,:n] = invA_11 + mul(mul(mul(invA_11,A_12), invS),mul(A_21, invA_11))
    C[:n,n:] = -1 * mul(mul(invA_11,A_12), invS)
    C[n:,:n] = -1 * mul(mul(invS,A_21), invA_11)
    C[n:,n:] = invS
    return C

if __name__ == "__main__":
    A = np.array([[Number(2),Number(3)],[Number(1),Number(2)]], dtype=Number)
    print(reverse_matrix(A))

