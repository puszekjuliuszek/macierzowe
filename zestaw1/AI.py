from Number import Number
import numpy as np

def AMU(A,B): # AI Matrix Multipication
    # TODO serio zrobić to dobrze

    if len(A) == 1:
        return A@B
    if len(A[0]) == 1 or len(B[0]) == 1:
        return A@B

    # macierz A jest rozmiaru 4n x 5m, macierz B będzie rozmiaru 5m x 5k , C nam wyjdzie 4n x 5k
    n = len(A) // 4
    m = len(A[0]) // 5
    k = len(B[0]) // 5

    a11, a12, a13, a14, a15 = A[:n,:m], A[:n,m:2*m], A[:n,2*m:3*m],A[:n,3*m:4*m], A[:n,4*m:]
    a21, a22, a23, a24, a25 = A[n:2*n,:m], A[n:2*n,m:2*m], A[n:2*n,2*m:3*m],A[n:2*n,3*m:4*m], A[n:2*n,4*m:]
    a31, a32, a33, a34, a35 = A[2*n:3*n,:m], A[2*n:3*n,m:2*m], A[2*n:3*n,2*m:3*m],A[2*n:3*n,3*m:4*m], A[3*n:,4*m:]
    a41, a42, a43, a44, a45 = A[3*n:,:m], A[3*n:,m:2*m], A[3*n:,2*m:3*m],A[3*n:,3*m:4*m], A[3*n:,4*m:]

    b11, b12, b13, b14, b15 = B[:m,:k], B[:m,k:2*k], B[:m,2*k:3*k],B[:m,3*k:4*k], B[:m,4*k:]
    b21, b22, b23, b24, b25 = B[m:2*m,:k], B[m:2*m,k:2*k], B[m:2*m,2*k:3*k],B[m:2*m,3*k:4*k], B[m:2*m,4*k:]
    b31, b32, b33, b34, b35 = B[2*m:3*m,:k],B[2*m:3*m,k:2*k], B[2*m:3*m,2*k:3*k],B[2*m:3*m,3*k:4*k], B[3*m:4*m,4*k:]
    b41, b42, b43, b44, b45 = B[3*m:4*m,:k], B[3*m:4*m,k:2*k], B[3*m:4*m,2*k:3*k],B[3*m:4*m,3*k:4*k], B[3*m:4*m,4*k:]
    b51, b52, b53, b54, b55 = B[4*m:,:k], B[4*m:,k:2*k], B[4*m:,2*k:3*k],B[4*m:,3*k:4*k], B[4*m:,4*k:]

    h1 = AMU(a32 , -b21 - b25 - b31)
    h2 = AMU(a22 + a25 - a35, -b25 - b51)
    h3 = AMU(-a31 - a41 + a42, -b11 + b25)
    h4 = AMU(a12 + a14 + a34, -b25 - b41)
    h5 = AMU(a15 + a22 + a25, -b24 + b51)
    h6 = AMU(-a22 - a25 - a45, b23 + b51)
    h7 = AMU(-a11 + a41 - a42, b11 + b24)
    h8 = AMU(a32 - a33 - a43, -b23 + b31)
    h9 = AMU(-a12 - a14 + a44, b23 + b41)
    h10 = AMU(a22 + a25,  b51)
    h11 = AMU(-a21 - a41 + a42, -b11 + b22)
    h12 = AMU(a41 - a42, b11)
    h13 = AMU(a12 + a14 + a24, b22 + b41)
    h14 = AMU(a13 - a32 + a33, b24 + b31)
    h15 = AMU(-a12 - a14, b41)
    h16 = AMU(-a32 + a33, b31)
    h17 = AMU(a12 + a14 - a21 + a22 - a23 + a24 - a32 + a33 - a41 + a42,  b22)
    h18 = AMU(a21, b11 + b12 + b52)
    h19 = AMU(-a23, b31 + b32 + b52)
    h20 = AMU(-a15 + a21 + a23 - a25, -b11 - b12 + b14 - b52)
    h21 = AMU(a21 + a23 - a25, b52)
    h22 = AMU(a13 - a14 - a24, b11 + b12 - b14 - b31 - b32 + b34 + b44)
    h23 = AMU(a13, -b31 + b34 + b44)
    h24 = AMU(a15, -b44 - b51 + b54)
    h25 = AMU(-a11, b11 - b14)
    h26 = AMU(-a13 + a14 + a15, b44)
    h27 = AMU(a13 - a31 + a33, b11 - b14 + b15 + b35)
    h28 = AMU(-a34, -b35 - b41 - b45)
    h29 = AMU(a31, b11 + b15 + b35)
    h30 = AMU(a31 - a33 + a34, b35)
    h31 = AMU(-a14 - a15 - a34, -b44 - b51 + b54 - b55)
    h32 = AMU(a21 + a41 + a44, b13 - b41 - b42 - b43)
    h33 = AMU(a43, -b31 - b33)
    h34 = AMU(a44, -b31 + b41 + b43)
    h35 = AMU(-a45, b13 + b51 + b53)
    h36 = AMU(a23 - a25 - a45, b31 + b32 + b33 + b52)
    h37 = AMU(-a41 - a44 + a45,  b13)
    h38 = AMU(-a23 - a31 + a33 - a34, b35 + b41 + b42 + b45)
    h39 = AMU(-a31 - a41 - a44 + a45, b13 + b51 + b53 + b55)
    h40 = AMU(-a13 + a14 + a15 - a44, -b31 - b33 + b34 + b44)
    h41 = AMU(-a11 + a41 - a45, b13 + b31 + b33 - b34 + b51 + b53 - b54)
    h42 = AMU(-a21 + a25 - a35, -b11 - b12 - b15 + b41 + b42 + b45 - b52)
    h43 = AMU(a24, b41 + b42)
    h44 = AMU(a23 + a32 - a33, b22 - b31)
    h45 = AMU(-a33 + a34 - a43, b35 + b41 + b43 + b45 + b51 + b53 + b55)
    h46 = AMU(-a35, -b51 - b55)
    h47 = AMU(a21 - a25 - a31 + a35, b11 + b12 + b15 - b41 - b42 - b45)
    h48 = AMU(-a23 + a33, b22 + b32 + b35 + b41 + b42 + b45)
    h49 = AMU(-a11 - a13 + a14 + a15 - a21 - a23 + a24 + a25, -b11 - b12 + b14)
    h50 = AMU(-a14 - a24, b22 - b31 - b32 + b34 - b42 + b44)
    h51 = AMU(a22, b21 + b22 - b51)
    h52 = AMU(a42, b11 + b21 + b23)
    h53 = AMU(-a12, -b21 + b24 + b41)
    h54 = AMU(a12 + a14 - a22 - a25 - a32 + a33 - a42 + a43 - a44 - a45, b23)
    h55 = AMU(a14 - a44, -b23 + b31 + b33 - b34 + b43 - b44)
    h56 = AMU(a11 - a15 - a41 + a45, b31 + b33 - b34 + b51 + b53 - b54)
    h57 = AMU(-a31 - a41, -b13 - b15 - b25 - b51 - b53 - b55)
    h58 = AMU(-a14 - a15 - a34 - a35, -b51 + b54 - b55)
    h59 = AMU(-a33 + a34 - a43 + a44, b41 + b43 + b45 + b51 + b53 + b55)
    h60 = AMU(a25 + a45, b23 - b31 - b32 - b33 - b52 - b53)
    h61 = AMU(a14 + a34, b11 - b14 + b15 - b25 - b44 + b45 - b51 + b54 - b55)
    h62 = AMU(a21 + a41, b12 + b13 + b22 - b41 - b42 - b43)
    h63 = AMU(-a33 - a43, -b23 - b33 - b35 - b41 - b43 - b45)
    h64 = AMU(a11 - a13 - a14 + a31 - a33 - a34, b11 - b14 + b15)
    h65 = AMU(-a11 + a41, -b13 + b14 + b24 - b51 - b53 + b54)
    h66 = AMU(a11 - a12 + a13 - a15 - a22 - a25 - a32 + a33 - a41 + a42,  b24)
    h67 = AMU(a25 - a35, b11 + b12 + b15 - b25 - b41 - b42 - b45 + b52 + b55)
    h68 = AMU(a11 + a13 - a14 - a15 - a41 - a43 + a44 + a45, -b31 - b33 + b34)
    h69 = AMU(-a13 + a14 - a23 + a24, -b24 - b31 - b32 + b34 - b52 + b54)
    h70 = AMU(a23 - a25 + a43 - a45, -b31 - b32 - b33)
    h71 = AMU(-a31 + a33 - a34 + a35 - a41 + a43 - a44 + a45, -b51 - b53 - b55)
    h72 = AMU(-a21 - a24 - a41 - a44, b41 + b42 + b43)
    h73 = AMU(a13 - a14 - a15 + a23 - a24 - a25, b11 + b12 - b14 + b24 + b52 - b54)
    h74 = AMU(a21 - a23 + a24 - a31 + a33 - a34, b41 + b42 + b45)
    h75 = AMU(a12 + a14 - a22 - a25 - a31 + a32 + a34 + a35 - a41 + a42, b25)
    h76 = AMU(a13 + a33, -b11 + b14 - b15 + b24 + b34 - b35)

    C = np.zeros((4*n,5*k), dtype=Number)
    C[:n, :k] = -h10 + h12 + h14 - h15 - h16 + h53 + h5 - h66 - h7
    C[n:2 * n, :k] = h10 + h11 - h12 + h13 + h15 + h16 - h17 - h44 + h51
    C[2 * n:3 * n, :k] = h10 - h12 + h15 + h16 - h1 + h2 + h3 - h4 + h75
    C[3 * n:, :k] = -h10 + h12 - h15 - h16 + h52 + h54 - h6 - h8 + h9
    C[:n, k:2 * k] = h13 + h15 + h20 + h21 - h22 + h23 + h25 - h43 + h49 + h50
    C[n:2 * n, k:2 * k] = -h11 + h12 - h13 - h15 - h16 + h17 + h18 - h19 - h21 + h43 + h44
    C[2 * n:3 * n, k:2 * k] = -h16 - h19 - h21 - h28 - h29 - h38 + h42 + h44 - h47 + h48
    C[3 * n:, k:2 * k] = h11 - h12 - h18 + h21 - h32 + h33 - h34 - h36 + h62 - h70
    C[:n, 2 * k:3 * k] = h15 + h23 + h24 + h34 - h37 + h40 - h41 + h55 - h56 - h9
    C[n:2 * n, 2 * k:3 * k] = -h10 + h19 + h32 + h35 + h36 + h37 - h43 - h60 - h6 - h72
    C[2 * n:3 * n, 2 * k:3 * k] = -h16 - h28 + h33 + h37 - h39 + h45 - h46 + h63 - h71 - h8
    C[3 * n:, 2 * k:3 * k] = h10 + h15 + h16 - h33 + h34 + h34 - h35 - h37 - h54 + h6 + h8 - h9
    C[:n, 3 * k:4 * k] = -h10 + h12 + h14 - h16 + h23 + h24 + h25 + h26 + h5 - h66 - h7
    C[n:2 * n, 3 * k:4 * k] = h10 + h18 - h19 + h20 - h22 - h24 - h26 - h5 - h69 + h73
    C[2 * n:3 * n,3 * k:4 * k] = -h14 + h16 - h23 - h26 + h27 + h29 + h31 + h46 - h58 + h76
    C[3 * n:, 3 * k:4 * k] = h12 + h25 + h26 - h33 - h35 - h40 + h41 + h65 - h68 - h7
    C[:n, 4 * k:] = h15 + h24 + h25 + h27 - h28 + h30 + h31 - h4 + h61 + h64
    C[n:2 * n,4 * k:] = -h10 - h18 - h2 - h30 - h38 + h42 - h43 + h46 + h67 + h74
    C[ 3 * n:, 4 * k:] = -h10 + h12 - h15 + h28 + h29 - h2 - h30 - h3 + h46 + h4 - h75
    C[3 * n:,4 * k:] = -h12 - h29 + h30 - h34 + h35 + h39 + h3 - h45 + h57 + h59
    return C

if __name__ == "__main__":
    A = np.array([[Number(5),Number(2),Number(5),Number(2),Number(5)],
                  [Number(7),Number(2),Number(5),Number(2),Number(5)],
                  [Number(5), Number(2), Number(2), Number(2), Number(5)],
                  [Number(3), Number(2), Number(5), Number(1), Number(5)]],
                 dtype=Number)
    B = np.array([[Number(5),Number(2),Number(8),Number(2),Number(12),Number(5),Number(2),Number(5),Number(2),Number(5)],
                  [Number(4), Number(2), Number(5), Number(2), Number(5),Number(5),Number(2),Number(5),Number(2),Number(5)],
                  [Number(2), Number(2), Number(1), Number(2), Number(5),Number(5),Number(2),Number(5),Number(2),Number(5)],
                  [Number(5), Number(3), Number(5), Number(11), Number(5),Number(5),Number(2),Number(5),Number(2),Number(5)],
                  [Number(5), Number(2), Number(5), Number(2), Number(6),Number(5),Number(2),Number(5),Number(2),Number(5)]],
                 dtype=Number)
    print(AMU(A,B))
    print(Number.ADD_counter + Number.MUL_counter + Number.SUB_counter)