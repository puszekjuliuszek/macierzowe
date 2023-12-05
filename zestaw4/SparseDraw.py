import numpy as np
import matplotlib.pyplot as plt
def sparse_draw(matrix, title = ''):
    image = (matrix == 0)
    image = image.astype(int)  *255
    fig = plt.figure()
    n = len(matrix)//50
    fig.set_size_inches((n,n))
    plt.imshow(image,cmap = "gray", vmin=0, vmax=255)
    plt.title(title)
    plt.axis('off')
    plt.show()