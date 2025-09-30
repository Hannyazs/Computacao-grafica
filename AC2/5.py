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

square = np.array([[1,1],[1,4],[4,4],[4,1]])

theta = -np.pi/4
R = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta),  np.cos(theta)]])
square_r = square @ R.T

plot_shapes(square, square_r, "Ex5 - Rotação Quadrado")

labels = ["A'", "B'", "C'", "D'"]
print("Novos vértices (aprox):")
for label, (x, y) in zip(labels, square_r):
    print(f"{label}: ({x:.2f}, {y:.2f})")

#Novos vértices (aprox): A=[1.41,0] B=[3.54,2.12] C=[5.66,0] D=[3.54,-2.12]