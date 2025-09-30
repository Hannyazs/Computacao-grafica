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

P = np.array([[3,2]])
P = P + [1,-1]             # Translação
rot90 = np.array([[0,-1],[1,0]])
P = P @ rot90.T            # Rotação
P = P * 2                  # Escala

plot_shapes([[3,2]], P, "Ex9 - Composição de Transformações")
print("Novo ponto:", P)

#Novo ponto: [4,1] -> [-1,4] -> [-2,8]