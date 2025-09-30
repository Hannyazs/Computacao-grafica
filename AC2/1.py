import numpy as np
import matplotlib.pyplot as plt

def plot_shapes(original, transformed, title):
    plt.figure()
    plt.scatter(*zip(*original), label="Original")
    plt.scatter(*zip(*transformed), label="Transformado")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.axis("equal")
    plt.show()

P = np.array([[2,3]])
P_t = P + [4,-2]

plot_shapes(P, P_t, "Ex1 - Translação")
print("Novo ponto:", P_t)

#Novo ponto é [6,1]