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

rot90 = np.array([[0,-1],[1,0]])
P = np.array([[1,0]])
P_r = P @ rot90.T

plot_shapes(P, P_r, "Ex4 - Rotação 90°")
print("Novo ponto:", P_r)

# Muda para (0,1)