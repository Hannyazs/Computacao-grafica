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
k=2
sh_matrix = np.array([[1,k],[0,1]])
P_s = P @ sh_matrix.T

plot_shapes(P, P_s, "Ex8 - Cisalhamento Horizontal")
print("Novo ponto:", P_s)

#Novo ponto: [8,3]