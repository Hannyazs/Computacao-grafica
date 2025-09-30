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

P = np.array([[2,5]])
P_r = P * [-1,1]

plot_shapes(P, P_r, "Ex6 - Reflexão Y")
print("Novo ponto:", P_r)

#Novo ponto: [-2,5]