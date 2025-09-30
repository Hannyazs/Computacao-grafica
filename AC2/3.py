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
triangle_t2 = triangle * [2,0.5]

plot_shapes(triangle, triangle_t2, "Ex3 - Escala Não Uniforme")
print("Novos vértices:\n", triangle_t2)

#A=[2,0.5] B=[6,0.5] C=[4,2] Duplicou de largura e reduziu pela metade a altura