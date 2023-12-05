import numpy as np
import matplotlib.pyplot as plt
from collections import deque


def draw_tree(root, title=''):
    image = np.ones(root.matrix.shape)*255

    Q = deque()
    Q.append(root)
    while Q:
        v = Q.pop()
        if v.leaf:
            r = len(v.s)
            gray = 125
            image[v.row_min:v.row_max, v.col_min:v.col_min+r] = gray*np.ones((v.row_max - v.row_min, r))#np.zeros((v.row_max - v.row_min, min(r,v.col_max - v.col_min )))
            image[v.row_min:v.row_min + r, v.col_min:v.col_max] =gray*np.ones((r , v.col_max - v.col_min)) #np.zeros((min(r,v.row_max - v.row_min) , v.col_max - v.col_min))
            image[v.row_min, v.col_min:v.col_max] = np.zeros((1,v.col_max - v.col_min))
            image[v.row_max-1, v.col_min:v.col_max] = np.zeros((1,v.col_max - v.col_min))
            image[v.row_min:v.row_max,v.col_min] = np.zeros(v.row_max-v.row_min)
            image[v.row_min:v.row_max,v.col_max-1] = np.zeros(v.row_max-v.row_min)
        else:
            for i in range(2):
                for j in range(2):
                    Q.append(v.childs[i][j])
    n = (root.row_max - root.row_min)//50   
    fig = plt.figure()
    fig.set_size_inches((n,n))
    plt.axis('off')
    plt.imshow(image,cmap = "gray", vmin=0, vmax=255)
    plt.title(title)
    plt.show()