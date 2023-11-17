import numpy as np
from LU_factorisation import *
from Number import *

def recursive_det_plain(A):
    L, U = LU_factorise_plain(A)
    return U.diagonal().prod()

def recursive_det_opt1(A):
    L, U = LU_factorise_opt1(A)
    return U.diagonal().prod()

def recursive_det_opt2(A):
    L, U = LU_factorise_opt2(A)
    return U.diagonal().prod()

def recursive_det(A):
    L, U = LU_factorise(A)
    return U.diagonal().prod()


if __name__ == "__main__":
    A = gen_mat_of_size_2_power_k(2, False)
    print(recursive_det(A).astype("float64"))
    print(np.allclose(np.linalg.det(A), recursive_det(A).astype("float64")))
    B = gen_mat_of_size_2_power_k(6, False)
    print(np.allclose(np.linalg.det(B), recursive_det(B).astype("float64")))
