from Number import Number
import numpy as np

def SMU(A,B): # Strassen Matrix Multiplication
    if len(A) == 1:
        return A@B
    n= len(A)//2
    A_11, A_12, A_21, A_22 = A[:n,:n], A[:n,n:], A[n:,:n],A[n:,n:]
    B_11, B_12, B_21, B_22 = B[:n,:n], B[:n,n:], B[n:,:n],B[n:,n:]
    M1 = SMU(A_11+A_22, B_11+B_22)
    M2 = SMU(A_21+A_22, B_11)
    M3 = SMU(A_11, B_12-B_22)
    M4 = SMU(A_22, B_21-B_11)
    M5 = SMU(A_11 + A_12, B_22)
    M6 = SMU(A_21-A_11, B_11+B_12)
    M7 = SMU(A_12-A_22, B_21+B_22)
    C = np.zeros((2*n,2*n), dtype=Number)
    C[:n,:n] = M1 + M4 - M5 + M7
    C[:n,n:] = M3 + M5
    C[n:,:n] = M2 + M4
    C[n:,n:] = M1 - M2 + M3 + M6
    return C

if __name__ == "__main__":
    A = np.array([[Number(2),Number(1),Number(2),Number(4)],
                [Number(1),Number(2),Number(4),Number(2)],
                [Number(1),Number(2),Number(6),Number(4)],
                [Number(1),Number(1),Number(4),Number(2)]], dtype=Number)
    
    B = np.array([[Number(2),Number(1),Number(2),Number(4)],
                [Number(1),Number(2),Number(4),Number(2)],
                [Number(1),Number(2),Number(6),Number(4)],
                [Number(1),Number(1),Number(4),Number(2)]], dtype=Number)
    print(SMU(A,B))
    print(Number.ADD_counter)