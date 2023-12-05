import numpy as np 

def minimum_degree_permutation(matrix):
    n,m = matrix.shape
    ADJ = {i:set() for i in range(n)}
    for i in range(n):
        for j in range(m):
            if matrix[i][j] != 0 and i != j:
                ADJ[i].add(j)
    permutation = []
    for i in range(n):
        deg_min = m+1
        for v, adj in ADJ.items():
            if len(adj) < deg_min:
                v_min = v
                deg_min = len(adj)
        for v in ADJ:
            ADJ[v] = ADJ[v].difference([v_min])
        for u in ADJ[v_min]:
            ADJ[u] = (ADJ[u].union(ADJ[v_min].difference([u])))
        ADJ.pop(v_min)
        permutation.append(v_min)
    return permutation


if __name__ == "__main__":
    M = np.array([
        [1,1,1,1,1],
        [1,2,0,0,0],
        [1,0,3,0,0],
        [1,0,0,4,0],
        [1,0,0,0,5]
    ])
    print(minimum_degree_permutation(M))
