from sklearn.utils.extmath import randomized_svd
import numpy as np
from numpy.linalg import svd

class CompressTree:
    def __init__(self,matrix, row_min, row_max, col_min, col_max):
        self.matrix = matrix
        self.row_min = row_min
        self.row_max = row_max
        self.col_min = col_min
        self.col_max = col_max


        self.leaf = False
        '''
         UL | UR
        ----+----
         DL | DR
    
        '''
        self.childs = [[None, None], [None, None]]

    def make_leaf(self, U, Sigma, V):
            self.leaf = True
            self.u = U
            self.s = Sigma
            self.v = V

    def create_tree(self, r, epsylon):
        
        U, Sigma, V = randomized_svd(self.matrix[self.row_min:self.row_max, self.col_min: self.col_max], n_components=r)
        if self.row_max == self.row_min + r:
            self.make_leaf(U, Sigma, V)
        elif Sigma[r-1] <= epsylon:
            self.make_leaf(U, Sigma, V)
        else:
            rows = [self.row_min, (self.row_min + self.row_max)//2, self.row_max]
            cols = [self.col_min, (self.col_min + self.col_max)//2, self.col_max]
            for i in range(2):
                for j in range(2):
                    self.childs[i][j] = CompressTree(self.matrix, rows[i], rows[i+1], cols[j], cols[j+1])
                    self.childs[i][j].create_tree(r, epsylon)
    def decompress(self, dest_matrix):
        if self.leaf:
            r = len(self.s)
            sigma = np.zeros((r,r))
            np.fill_diagonal(sigma, self.s)
            dest_matrix[self.row_min:self.row_max, self.col_min: self.col_max] = self.u @ sigma @ self.v
        
        else:
            for i in range(2):
                for j in range(2):
                    self.childs[i][j].decompress(dest_matrix)

    def compare(self, new_matrix):
        return np.sum(np.square(self.matrix - new_matrix))

if __name__ == "__main__":
    X = np.random.random((64,64))
    P = np.random.random((64,64))
    P = (P > 0.8).astype(int)
    X = P * X
    X


    root = CompressTree(X, 0, len(X), 0, len(X[0]))
    U, Sigma, V = svd(X)
    Sigma
    root.create_tree(1, Sigma[len(Sigma)-1])

