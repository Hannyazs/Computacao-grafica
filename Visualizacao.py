import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(100)
y = np.random.rand(100)
z = np.random.rand(100)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")

pontos = ax.scatter(x, y, z, c=z, cmap="plasma", s=60, alpha=0.8, edgecolors="k")

cbar = fig.colorbar(pontos, ax=ax, shrink=0.5, aspect=10)
cbar.set_label("Intensidade (Z)", fontsize=10)

ax.set_title("Visualização Computacional - Gráfico 3D", fontsize=14, fontweight="bold")
ax.set_xlabel("Eixo X")
ax.set_ylabel("Eixo Y")
ax.set_zlabel("Eixo Z")

ax.view_init(elev=20, azim=135)

plt.show()
