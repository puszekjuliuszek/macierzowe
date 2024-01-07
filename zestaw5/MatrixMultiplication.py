from collections import deque
from CompressTree import CompressTree
import numpy as np
from numpy.linalg import svd
from sklearn.utils.extmath import randomized_svd

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

def _rSVD(A, B, d):
    Qa, Ra = np.linalg.qr(A)
    Qb, Rb = np.linalg.qr(B)
    U_prim, Sigma, V_prim = randomized_svd(Ra @ Rb, n_components=d)#svd(Ra @ Rb.T)
    print(f'    Qa {Qa.shape} Ra {Ra.shape} Qb {Qb.shape} Rb {Rb.shape}')
    print(f'   ', U_prim.shape, V_prim.shape)
    U = Qa @ U_prim @ np.diag(Sigma)
    V = V_prim @ Qb
    return U, V

def _rSVD(A, B, d):
    U, S, V = randomized_svd(A @ B, n_components=d)
    return U @ np.diag(S), V

def _add_compmatrix(u1, v1, u2, v2):
    A = np.append(u1, u2, axis = 1)
    B = np.append(v1, v2, axis=0)
    # print(u1.shape, u2.shape, v1.shape, v2.shape)
    # print(A.shape, B.shape)
    
    U,V =  _rSVD(A, B, u1.shape[1])
    # print(U.shape, V.shape)
    # print()
    return U,V

def _mul_compmatrix(u1, v1, u2, v2):
    temp = v1 @ u2
    U = u1 @ temp
    return U, v2

def _add_rekur(node1 : CompressTree, node2 : CompressTree) ->  CompressTree:
    result_node = CompressTree(None, None, None, None, None)
    
    if node1.leaf and node2.leaf:
        r = node1.u.shape[1]
        U, V = _add_compmatrix(node1.u  @ np.diag(node1.s), node1.v, node2.u @ np.diag(node2.s), node2.v)
        result_node.make_leaf(U, np.ones((r,)), V)
        return result_node
    
    elif node1.leaf or node2.leaf:
        node = node1 if node1.leaf else node2

        n = node.row_max - node.row_min
        r = node.u.shape[1]
        
        u_part = [node.u[:n//2], node.u[n//2:]]
        v_part = [node.v[:n//2], node.v[n//2:]]
        
        for i in range(2):
            for j in range(2):
                fake_child = CompressTree(None, None, None, None, None)
                fake_child.make_leaf(u_part[i], np.ones((r,)), v_part[j])
                if node1.leaf:
                    result_node.childs[i][j] = _add_rekur(fake_child, node2.childs[i][j])
                else:
                    result_node.childs[i][j] = _add_rekur(node1.childs[i][j], fake_child)
    
    else:
        for i in range(2):
            for j in range(2):
                result_node.childs[i][j] = _add_rekur(node1.childs[i][j], node2.childs[i][j])
        
    return result_node

def _normalize_root(root, root1):
    n = root1.matrix.shape[0]
    root.row_min = 0
    root.row_max = n
    root.col_min = 0
    root.col_max = n
    M = np.zeros((n,n))
    Q = deque()
    Q.append(root)
    while Q:
        node : CompressTree = Q.popleft()
        node.matrix = M
        rows = [node.row_min, (node.row_min + node.row_max)//2, node.row_max]
        cols = [node.col_min, (node.col_min + node.col_max)//2, node.col_max]
        for i in range(2):
            for j in range(2):
                if not node.leaf:
                    node.childs[i][j].row_min = rows[i]
                    node.childs[i][j].row_max = rows[i+1]
                    node.childs[i][j].col_min = cols[j]
                    node.childs[i][j].col_max = cols[j+1]
                    Q.append(node.childs[i][j])
    root.decompress(M)

def add_compmatrix(root1 : CompressTree, root2 : CompressTree):
    result = _add_rekur(root1, root2)
    _normalize_root(result, root1)
    return result

def _mul_rekur(node1 : CompressTree, node2 : CompressTree) ->  CompressTree:
    result_node = CompressTree(None, None, None, None, None)
    if node1.leaf and node2.leaf:
        r = node1.u.shape[1]
        U, V = _mul_compmatrix(node1.u @ np.diag(node1.s), node1.v, node2.u @ np.diag(node2.s), node2.v)
        result_node.make_leaf(U, np.ones((1, r)), V)

    elif node1.leaf or node2.leaf:
        
        node = node1 if node1.leaf else node2

        n = node.row_max - node.row_min
        r = node.u.shape[1]
        
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

                child = add_compmatrix(first, second)
                result_node.childs[i][j] = child

    else:
        for i in range(2):
            for j in range(2):
                first = _mul_rekur(node1.childs[i][0], node2.childs[0][j])
                second = _mul_rekur(node1.childs[i][1], node2.childs[1][j])

                child = add_compmatrix(first, second)
                result_node.childs[i][j] = child
    return result_node



def mul_compmatrix(root1 : CompressTree, root2 : CompressTree):

    result = _mul_rekur(root1, root2)
    _normalize_root(result, root1)
    return result




if __name__ == '__main__':

    def gen_matrix(n, d = 0.7):
        X = np.random.random((n,n))
        P = np.random.random((n,n))
        P = (P > d).astype(int)
        return X * P

    n = 8
    M = gen_matrix(n, 0.8)
    # M = np.array([[ 0,0,2,0],
    #     [ 0,0,0,0],
    #     [ 8,0,10,11],
    #     [12,13,0,0]])
    print(M)
    
    root = CompressTree(M, 0, len(M), 0, len(M[0]))
    vector = np.array([[j] for j in range(n)])
    U, Sigma, V = svd(M)
    root.create_tree(1, Sigma[-1])

    # print(sum(compmatrix_mul_vector(root , vector) - M @ vector))
    result = mul_compmatrix(root, root)
    N = np.zeros_like(M)
    root.decompress(N)
    print(N)
    result.decompress(N)
    print()
    print()
    print()
    # print(N)
    print((M @ M)-N)
    print(np.sum(np.abs((M @ M)-N)))

