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

triangle2 = np.array([[2,3],[4,3],[3,5]])
triangle2_r = triangle2 * [1,-1]

plot_shapes(triangle2, triangle2_r, "Ex7 - Reflexão X")
print("Novos vértices:\n", triangle2_r)

#Novos vértices: A=[2,-3] B=[4,-3] C=[3,-5]