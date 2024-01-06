import numpy as np
import matplotlib.pyplot as plt

from MatrixGenerator import generate_3d_matrix


def sparse_draw(matrix, title = ''):
    image = (matrix == 0)
    image = image.astype(int)  *255
    fig = plt.figure()
    n = len(matrix)//50
    fig.set_size_inches((n,n))
    plt.imshow(image,cmap = "gray", vmin=0, vmax=255)
    plt.title(title)
    plt.axis('off')
    # plt.figure(figsize=(10, 6))
    plt.show()

if __name__ == "__main__":
    X = generate_3d_matrix(2)
    sparse_draw(X, f"wzorzec rzadkości przed kompresją i permutacją\n dla algo {1} sigmy {1} k {2}")