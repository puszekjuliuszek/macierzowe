import numpy as np

def _stamp(P, jump):
    n = len(P)
    for i in range(jump, n):
        P[i][i - jump] = 1
    for i in range(n-jump):
        P[i][i+jump] = 1

def generate_3d_matrix(k):
    n = 2**(k*3)
    X = np.random.random((n, n))
    P = np.zeros_like(X)
    jumps = [0] + [2**(i*k) for i in range(3)]
    for jump in jumps:
        _stamp(P, jump)
    return X * P


if __name__ == "__main__":
    generate_3d_matrix(2)


                