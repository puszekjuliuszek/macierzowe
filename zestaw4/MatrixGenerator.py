import numpy as np

def generate_3d_matrix(k):
    n = 2**(k*3)
    X = np.random.random((n, n))
    P = np.zeros_like(X)
    big_jump = 2**(2*k)
    small_jump = 2**k
    jumps = [0] + [2**(i*k) for i in range(3)]
    for a in range(2**k):
        A = big_jump * a
        for b in range(2**k):
            B = small_jump * b
            for c in range(2**k):
                v = P[A + B + c]
                if a > 0:
                    v[A + B + c - big_jump] = 1
                if a < 2**k - 1:
                    v[A + B + c + big_jump] = 1
                if b > 0:
                    v[A + B + c - small_jump] = 1
                if b < 2**k - 1:
                    v[A + B + c + small_jump] = 1
                if c > 0:
                    v[A + B + c - 1] = 1
                if c < 2**k - 1:
                    v[A + B + c + 1] = 1
                
    return X * P


if __name__ == "__main__":
    generate_3d_matrix(2)


                