import numpy as np
import matplotlib.pyplot as plt

red = np.random.rand(200, 200)
green = np.random.rand(200, 200)
blue = np.random.rand(200, 200)
nir = np.random.rand(200, 200)

rgb = np.dstack((red, green, blue))
false_color = np.dstack((nir, red, green))

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.title("RGB")
plt.imshow(rgb)
plt.axis("off")

plt.subplot(1,2,2)
plt.title("False Color")
plt.imshow(false_color)
plt.axis("off")

plt.show()
