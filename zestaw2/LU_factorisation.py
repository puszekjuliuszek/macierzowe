import numpy as np
from Number import Number
from reverse_matrix import reverse_matrix
from Strassen import SMU as mul

def LU_factorise(A):
    if len(A) == 1:
        return np.array([[Number(1)]],dtype=Number), A
    n = len(A)//2
    A_11, A_12, A_21, A_22 = A[:n,:n], A[:n,n:], A[n:,:n],A[n:,n:]
    L_11, U_11 = LU_factorise(A_11)
    invU_11 = reverse_matrix(U_11, "U")
    L_21 = mul(A_21, invU_11)
    invL_11 = reverse_matrix(L_11, "L")
    U_12 = mul(invL_11, A_12)
    S = A_22 - mul(L_21, U_12)
    L_22, U_22 = LU_factorise(S)
    L, U = np.zeros((2*n,2*n), dtype=Number), np.zeros((2*n,2*n), dtype=Number)
    L[:n,:n], L[n:,:n], L[n:,n:] = L_11, L_21, L_22
    U[:n,:n], U[:n,n:], U[n:,n:] = U_11, U_12, U_22
    return L, U

if __name__ == "__main__":
    A = np.array([[Number(2),Number(1),Number(2),Number(4)],
                  [Number(1),Number(2),Number(4),Number(2)],
                  [Number(1),Number(2),Number(6),Number(4)],
                  [Number(1),Number(1),Number(4),Number(2)]], dtype=Number)
    print(LU_factorise(A))
