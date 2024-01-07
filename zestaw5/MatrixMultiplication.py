from collections import deque
from CompressTree import CompressTree
import numpy as np
from numpy.linalg import svd

def _matxvec_rekur(node : CompressTree, vector : np.array):
    if node.leaf:
        a = node.v @ vector
        b = node.u @ a 
        c = b * node.s[0]
        return (node.u @ (node.v @ vector)) * node.s[0]
    else:
        n = len(vector)
        upper, lower = vector[:n//2], vector[n//2:]
        out_upper = _matxvec_rekur(node.childs[0][0], upper) + _matxvec_rekur(node.childs[0][1], lower)
        out_lower = _matxvec_rekur(node.childs[1][0], upper) + _matxvec_rekur(node.childs[1][1], lower)
        return np.append(out_upper, out_lower, axis=0)


def compmatrix_mul_vector(root : CompressTree, vector : np.array):
    if vector.shape[0] == 1 and vector.shape[1] > 1:
        vector = vector.T
    if vector.shape[1] != 1 and vector.shape[0] != root.col_max - root.col_min:
        raise ValueError('wrong vector')
    
    return _matxvec_rekur(root, vector)

def _rSVD(A, B):
    Qa, Ra = np.linalg.qr(A)
    Qb, Rb = np.linalg.qr(B)
    U_prim, Sigma, V_prim = svd(Ra @ Rb.T)
    U = Qa @ U_prim
    V = Qb @ V_prim
    return U, V

def _add_compmatrix(u1, v1, u2, v2):
    A = np.append(u1, u2)
    B = np.append(v1, v2, axis=0)
    return _rSVD(A, B)

def _mul_compmatrix(u1, v1, u2, v2):
    temp = v1 @ u2
    U = u1 @ temp
    return U, v2

def _mul_rekur(node1 : CompressTree, node2 : CompressTree, result_node : CompressTree):
    if node1.leaf and node2.leaf:
        U, V = _mul_compmatrix(node1.u @ np.diag(), node1.v, node2.u, node2.v)
        result_node.make_leaf(U, np.ones((1,1)), V)
    elif node1.leaf or node2.leaf:
        rows = [result_node.row_min, (result_node.row_min + result_node.row_max)//2, result_node.row_max]
        cols = [result_node.col_min, (result_node.col_min + result_node.col_max)//2, result_node.col_max]
        n = result_node.row_max - result_node.row_min
        r = node1.u.shape[1]
        node = node1 if node1.leaf else node2

        u_part = [node.u[:n//2], node.u[n//2:]]
        v_part = [node.v[:n//2], node.v[n//2:]]
        fake_childs = [[None for _ in range(2)] for _ in range(2)]
        for i in range(2):
            for j in range(2):
                fake_childs[i][j] = CompressTree(None, None, None, None, None)
                fake_childs[i][j].make_leaf(u_part[i], np.ones((1, r)), v_part[j])

        for i in range(2):
            for j in range(2):
                if node1.leaf:
                    first = _mul_rekur(fake_childs[i][0], node2.childs[0][j])
                    second = _mul_rekur(fake_childs[i][1], node2.childs[1][j])
                else:
                    first = _mul_rekur(node1.childs[i][0], fake_childs[0][j])
                    second = _mul_rekur(node1.childs[i][1], fake_childs[1][j])
                U, V = _add_compmatrix(first, second)

                result_node.childs[i][j] = CompressTree(None, rows[i], rows[i+1], cols[j], cols[j+1])
                result_node.childs[i][j].make_leaf(U, np.ones((1, r)), V)



                


def mul_compmatrix(root1 : CompressTree, root2 : CompressTree):

    result = CompressTree(None, root1.row_min, root1.row_max, root1.col_min, root1.col_max)
    _mul_rekur(root1, root2, result)



if __name__ == '__main__':

    def gen_matrix(n, d = 0.7):
        X = np.array([[i*n + j for j in range(n)] for i in range(n)])
        P = np.random.random((n,n))
        P = (P > d).astype(int)
        return X * P

    n = 8
    M = gen_matrix(n, 0.7)
    print(M)
    
    root = CompressTree(M, 0, len(M), 0, len(M[0]))
    vector = np.array([[j] for j in range(n)])
    U, Sigma, V = svd(M)
    root.create_tree(1, Sigma[-1])
    

    print(sum(compmatrix_mul_vector(root , vector) - M @ vector))
    print()


