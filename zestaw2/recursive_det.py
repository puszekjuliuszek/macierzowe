import numpy as np
from LU_factorisation import LU_factorise
from Number import Number
def recursive_det(A):
    L, U = LU_factorise(A)
    return U.diagonal().prod()


if __name__ == "__main__":

    A = np.array([[Number(2),Number(1)],[Number(1),Number(2)]], dtype=Number)
    print(LU_factorise(A)[0],'\n\n', LU_factorise(A)[1])
    print(recursive_det(A))
