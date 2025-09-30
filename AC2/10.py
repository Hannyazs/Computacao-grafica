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

rect = np.array([[1,1],[5,1],[5,3],[1,3]])
rect = rect + [-2,3]       # Translação
rect = rect * [1.5,0.5]    # Escala
rect_r = rect * [-1,1]     # Reflexão Y

plot_shapes([[1,1],[5,1],[5,3],[1,3]], rect_r, "Ex10 - Retângulo Transformado")
print("Novos vértices:\n", rect_r)

#Novo ponto: [−1,4],[3,4],[3,6],[−1,6] -> [−1.5,2],[4.5,2],[4.5,3],[−1.5,3] -> [1.5,2],[−4.5,2],[−4.5,3],[1.5,3]