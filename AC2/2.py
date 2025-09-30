import numpy as np
import matplotlib.pyplot as plt

def plot_shapes(original, transformed, title):
    plt.figure()
    plt.plot(*zip(*original, original[0]), label="Original")
    plt.plot(*zip(*transformed, transformed[0]), "--", label="Transformado")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.axis("equal")
    plt.show()

triangle = np.array([[1,1],[3,1],[2,4]])
triangle_t = triangle * 2

plot_shapes(triangle, triangle_t, "Ex2 - Escala Uniforme")
print("Novos vértices:\n", triangle_t)

#A=[2,2] B=[6,2] C=[4,8] Duplicou de tamanho